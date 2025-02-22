import logging
from enum import Enum
from pathlib import Path
from typing import Optional, List, Dict, Any, Union, TextIO

import pandas as pd
import yaml
from pydantic import BaseModel, Field, ConfigDict

logger = logging.getLogger(__name__)

FormatString = str
TemplateName = str
Metric = str
Hyperparameter = str


class StrictBaseModel(BaseModel):
    """
    Base class for Pydantic models that forbids extra fields.
    """
    model_config = ConfigDict(extra="forbid")

    def as_flat_dict(self, simple=True, prefix = None) -> Dict[str, Any]:
        """
        Convert the model to a flat dictionary.

        Suitable for conversion to a DataFrame.

        :param simple:
        :param prefix:
        :return:
        """
        def is_complex(v):
            if isinstance(v, dict):
                return True
            if isinstance(v, list) and any(isinstance(i, dict) for i in v):
                return True
            return False
        def mk_key(k):
            if prefix:
                return f"{prefix}_{k}"
            return k
        d = {mk_key(k): v for k, v in self.model_dump().items() if not is_complex(v)}
        return d

class MetricEnum(Enum):
    """
    Enum for metrics to be evaluated.

    Designed to be extensible.
    """
    QA_WITH_EXPLANATION = "qa_with_explanation"
    SIMPLE_QUESTION = "simple_question"
    LIST_MEMBERSHIP = "list_membership"
    RANKED_LIST = "ranked_list"
    NARRATIVE_SIMILARITY = "narrative_similarity"
    REVIEW = "review"
    BLEU = "bleu"
    ROUGE = "rouge"
    METEOR = "meteor"

class Response(StrictBaseModel):
    """
    Response from the AI model.
    """
    text : str = Field(..., description="The text of the response from the AI model")
    prompt: Optional[str] = Field(None, description="The prompt used to generate the response")
    system: Optional[str] = Field(None, description="The system prompt used to generate the response")


class Template(StrictBaseModel):
    """
    Template for generating prompts to the AI model.
    """
    system: Optional[FormatString] = Field(None, description="System prompt")
    prompt: Optional[FormatString] = Field(None, description="Prompt format string to the model")
    metrics: Optional[List[Metric]] = Field(None, description="Metrics to be evaluated")

class Matrix(StrictBaseModel):
    """
    Specifies a combination of hyperparameters to be evaluated.
    """
    hyperparameters: Dict[Hyperparameter, List[Any]] = Field(..., description="Hyperparameters to be evaluated")
    exclude: Optional["Matrix"] = Field(None, description="Hyperparameters to be excluded")

class TestCase(StrictBaseModel):
    """
    Test case for the AI model.
    """
    input: str = Field(..., description="Input to the model")
    original_input: Optional[Dict[str, Any]] = Field(
        None,
        description="""Original input to the model, prior to transformation into text.
        An example is a structured data record.
        """
    )
    #output: Optional[str] = Field(None, description="Provided output from the model")
    ideal: Optional[str] = Field(None, description="Ideal output from the model")
    template: Optional[TemplateName] = Field(None, description="Template for the test case")
    tags: Optional[List[str]] = Field(None, description="Tags for the test case")
    comments: Optional[List[str]] = Field(None, description="Comments for the test case")

    def as_flat_dict(self, **kwargs) -> Dict[str, Any]:
        top_dict = super().as_flat_dict(**kwargs)
        orig = self.original_input or {}
        return {**top_dict, **orig}


class TestCaseResult(StrictBaseModel):
    """
    Result of running an individual case on a model with hyperparameters.
    """
    case: TestCase = Field(..., description="Test case")
    response: Response = Field(..., description="Response from the model")
    hyperparameters: Dict[Hyperparameter, Any] = Field(..., description="Hyperparameters used for the test case")
    metrics: Optional[List[Metric]] = Field(None, description="Metrics to be evaluated")
    score: Optional[float] = Field(None, description="Score for the test case", ge=0, le=1)
    evaluation_message: Optional[str] = Field(None, description="Message from the evaluation")

    def as_flat_dict(self, **kwargs) -> Dict[str, Any]:
        top_dict = super().as_flat_dict(**kwargs)
        case_dict = self.case.as_flat_dict(prefix="case")
        response_dict = self.response.as_flat_dict(prefix="response")
        hyperparameters_dict = {k: str(v) for k, v in self.hyperparameters.items()}
        hyperparameters_str = "_".join(f"{k}={v}" for k, v in hyperparameters_dict.items())
        return {"hyperparameters": hyperparameters_str, **top_dict, **case_dict, **response_dict, **hyperparameters_dict}

class ModelInfo(StrictBaseModel):
    plugins: Optional[List[str]] = Field(None, description="List of plugins for the model")
    parameters: Dict[str, Any] = Field({}, description="Parameters for the model")

class Suite(StrictBaseModel):
    name: str = Field(..., description="Name of the test suite")
    version: Optional[str] = Field(None, description="Version of the test suite")
    description: Optional[str] = Field(None, description="Description of the test suite")
    comments: Optional[List[str]] = Field(None, description="Comments for the test case")
    models: Dict[str, ModelInfo] = Field({}, description="Models to be evaluated")
    matrix: Matrix = Field(..., description="Matrix of hyperparameters")
    cases: List[TestCase] = Field(..., description="Test cases")
    template: Optional[TemplateName] = Field(None, description="Template for the test case")
    templates: Optional[Dict[TemplateName, Template]] = Field(None, description="Templates for the test cases")

def load_suite(input_path: Union[str, Path, TextIO], syntax="yaml") -> Suite:
    if isinstance(input_path, str):
        input_path = Path(input_path)
    if isinstance(input_path, Path):
        with input_path.open() as f:
            return load_suite(f, syntax=syntax)
    if syntax != "yaml":
        raise NotImplementedError(f"Syntax {syntax} not implemented")
    obj = yaml.safe_load(input_path)
    logger.info(f"Loaded suite from {input_path}")
    return Suite(**obj)

def results_to_dataframe(results: List[TestCaseResult]) -> pd.DataFrame:
    flat_results = [r.as_flat_dict() for r in results]
    return pd.DataFrame(flat_results)

