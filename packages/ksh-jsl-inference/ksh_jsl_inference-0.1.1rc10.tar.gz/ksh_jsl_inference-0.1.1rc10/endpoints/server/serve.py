import uvicorn
from endpoints.log_utils import logger
from fastapi import FastAPI
from typing import Optional, List
from endpoints.settings import JSL_DOWNLOAD_PACKAGES, DEFAULT_JOHNSNOWLABS_VERSION

from endpoints.johnsnowlabs.inference.model import BaseInferenceModel
from endpoints.johnsnowlabs.inference.medical_nlp_model import MedicalNlpInferenceModel
from endpoints.pip_utils import install
from endpoints import Platform, Recipe
from endpoints.log_utils import configure_logging
from .routers import healthcheck


def create_fast_api_app(
    inference_model: BaseInferenceModel,
    include_sagemaker_route=False,
    include_snowflake_route=False,
):
    from contextlib import asynccontextmanager

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        inference_model.predict({inference_model._input._field: "Sample request"})

        yield {"model": inference_model}

        inference_model.dispose()

    app = FastAPI(lifespan=lifespan)
    configure_logging()

    app.include_router(healthcheck.router)
    if include_sagemaker_route:
        from .routers import sagemaker

        app.include_router(sagemaker.router)
    if include_snowflake_route:
        from .routers import snowflake

        app.include_router(snowflake.router)
    return app


def get_requirements(
    platform: Platform,
    johnsnowlabs_version: Optional[str] = None,
    inference: Optional[BaseInferenceModel] = None,
) -> List[str]:
    """
    Generates a list of requirements  for the specified platform and inference model.

    :param str johnsnowlabs_version: The version of the John Snow Labs library.
    :param Platform platform: The platform for which the requirements are being generated.
    :param BaseInferenceModel inference: The inference model to include in the requirements.

    Returns:
        List[str] : A list of requirements.
    """
    requirements = []
    if johnsnowlabs_version:
        requirements = [f"johnsnowlabs=={johnsnowlabs_version}"]

    additional_packages = platform.get_python_requirements()
    if inference:
        additional_packages.extend(inference.get_python_requirements())
    additional_packages = [
        package
        for package in additional_packages
        if not package.startswith("johnsnowlabs")
    ]
    ##TODO: Add checks for requirements conflicts
    requirements.extend(additional_packages)

    return requirements


def install_python_requirements(
    platform: Platform,
    inference_model: BaseInferenceModel,
    johnsnowlabs_version: Optional[str] = None,
):
    if not JSL_DOWNLOAD_PACKAGES:
        logger.info("Skipping installation of python requirements")
    else:
        requirements = get_requirements(
            platform=platform,
            inference=inference_model,
            johnsnowlabs_version=johnsnowlabs_version,
        )
        install(requirements)
