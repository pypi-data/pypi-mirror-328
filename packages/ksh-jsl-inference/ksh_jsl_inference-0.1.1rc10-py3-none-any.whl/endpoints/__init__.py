"""JSL Inference Module"""

from enum import Enum


class Recipe(str, Enum):
    HEALTHCARE_NLP = "healthcare_nlp"
    VISUAL_NLP = "visual_nlp"
    LLM = "llm"
    CHROMADB_RESOLVER = "chromadb_resolver"

    def get_default_inference_model(self):
        if self == Recipe.HEALTHCARE_NLP:
            from endpoints.johnsnowlabs.inference.medical_nlp_model import (
                MedicalNlpInferenceModel,
            )

            return MedicalNlpInferenceModel()
        elif self == Recipe.CHROMADB_RESOLVER:
            from endpoints.johnsnowlabs.inference.chroma_resolver_model import (
                ChromaDbResolverInferenceModel,
            )

            return ChromaDbResolverInferenceModel()
        else:
            raise NotImplementedError(f"Recipe '{self}' is not implemented.")


class Platform(str, Enum):
    SAGEMAKER = "sagemaker"
    SNOWFLAKE = "snowflake"

    def get_python_requirements(self):
        if self == Platform.SNOWFLAKE:
            return ["snowflake-snowpark-python"]
        return []


class JslInferenceException(Exception):
    """Exception for JSL Inference errors"""

    pass
