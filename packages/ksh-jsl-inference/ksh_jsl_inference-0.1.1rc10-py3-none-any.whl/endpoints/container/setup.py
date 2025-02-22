import shutil
from endpoints.container.utils import (
    install_johnsnowlabs_from_docker_secret,
)
from endpoints.log_utils import configure_logging, logger
import os
from typing import Optional
from endpoints.settings import TARGET_PLATFORM

from endpoints.johnsnowlabs.inference.model import BaseInferenceModel
from endpoints.server import setup_env


def _cleanup_container():
    home_dir = os.path.expanduser("~")
    paths_to_remove = [
        os.path.join(home_dir, "cache_pretrained"),
        os.path.join(home_dir, ".javacpp"),
        os.path.join("/tmp"),
    ]
    for path in paths_to_remove:
        shutil.rmtree(path, ignore_errors=True)


def setup_container_env(
    inference_model: BaseInferenceModel,
    model: Optional[str] = None,
    language: str = "en",
    johnsnowlabs_version: Optional[str] = None,
    store_license: bool = True,
):
    """
    Setup the environment for serving the model.

    :param BaseInferenceModel inference_model: The inference model to be used.
    :param str model: The model to be used. If not provided, the model will not be downloaded.
    :param str language: The language of the model.
    :param str johnsnowlabs_version: The version of the John Snow Labs library to install.
    :param bool store_license: Flag indicating if the license should be stored in the container. Default: True

    Example:

    .. code-block:: python

            from endpoints.container import setup_container_env
            from endpoints.johnsnowlabs.inference.medical_nlp_model import MedicalNlpInferenceModel

            setup_container_env(
                inference_model=MedicalNlpInferenceModel(),
                model="clinical_deidentification"
            )
    """

    configure_logging()
    install_johnsnowlabs_from_docker_secret()
    setup_env(
        platform=TARGET_PLATFORM,
        inference_model=inference_model,
        model=model,
        language=language,
        johnsnowlabs_version=johnsnowlabs_version,
    )
    if not store_license:
        logger.info("Removing the licenses")
        shutil.rmtree(
            f"/{os.path.expanduser('~')}/.johnsnowlabs/licenses", ignore_errors=True
        )

    _cleanup_container()
