import uvicorn
from typing import Optional

from endpoints.johnsnowlabs.inference.model import BaseInferenceModel
from endpoints.johnsnowlabs.inference.medical_nlp_model import MedicalNlpInferenceModel
from endpoints import Platform, Recipe
from .serve import create_fast_api_app, install_python_requirements


def serve(
    platform: Platform,
    port: int = 8080,
    inference_model: Optional[BaseInferenceModel] = None,
):
    """
    Serve the model for inferencing

    :param str platform: The platform for which the container is being served.
    :param int port: The port on which the container should be served.
    :param BaseInferenceModel inference_model: The inferencing logic to use..
    """
    if not inference_model:
        inference_model = MedicalNlpInferenceModel()

    app = create_fast_api_app(
        inference_model,
        include_sagemaker_route=(platform == Platform.SAGEMAKER),
        include_snowflake_route=(platform == Platform.SNOWFLAKE),
    )

    uvicorn.run(app, host="0.0.0.0", port=port)


def setup_env(
    platform: Platform,
    inference_model: BaseInferenceModel,
    model: Optional[str],
    language: str = "en",
    recipe: Recipe = Recipe.HEALTHCARE_NLP,
    johnsnowlabs_version: Optional[str] = None,
):
    """
    Install the required packages and download the model and setup the environment

    :param str platform: The platform for which the container is being served.
    :param BaseInferenceModel inference_model: The inferencing logic to use.
    :param str model: The model to download. If None, no model is downloaded.
    :param str language: The language of the model to download. Default: 'en'.
    :param Recipe recipe: The recipe to use for the model. Default: Recipe.HEALTHCARE_NLP.
    :param str johnsnowlabs_version: The version of the John Snow Labs library.
    """
    install_python_requirements(platform, inference_model, johnsnowlabs_version)
    if model:
        from endpoints.model import download_model

        download_model(
            model=model,
            language=language,
            recipe=recipe,
        )


def setup_env_and_start_server(
    platform: Platform,
    model: Optional[str] = None,
    recipe: Recipe = Recipe.HEALTHCARE_NLP,
    inference_model: Optional[BaseInferenceModel] = None,
    language: str = "en",
    port: int = 8080,
):
    """
    Setup the environment and start the inferencing server

    :param str platform: The platform for which the container is being served.
    :param str model: The model to download. If None, no model is downloaded.
    :param Recipe recipe: The recipe to use for the model.
    :param BaseInferenceModel inference_model: The inferencing logic to use.
    :param str language: The language of the model to download. Default: 'en'.
    :param int port: The port on which the container should be served. Default: 8080.
    """
    inference_model_obj = inference_model or recipe.get_default_inference_model()
    setup_env(
        model=model,
        recipe=recipe,
        inference_model=inference_model_obj,
        language=language,
        platform=platform,
    )
    serve(
        platform=platform,
        port=port,
        inference_model=inference_model_obj,
    )
