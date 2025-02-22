from enum import Enum


class Platform(str, Enum):
    """
    All supported platforms.
    """

    SAGEMAKER = "sagemaker"
    SNOWFLAKE = "snowflake"

    def get_python_requirements(self):
        """
        Return the python packages dependencies for the given platform.
        """
        if self == Platform.SNOWFLAKE:
            return ["snowflake-snowpark-python"]
        return []


class Recipe(str, Enum):
    """
    All supported recipes.
    """

    HEALTHCARE_NLP = "healthcare_nlp"
    VISUAL_NLP = "visual_nlp"
    LLM = "llm"
    CHROMADB_RESOLVER = "chromadb_resolver"

    def get_default_inference_model(self):
        """
        Return the default inference model for the given recipe.
        """
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
