import os
from endpoints import Platform


MODEL_LOCATION = "/opt/ml/model"
HOME_DIR = os.path.expanduser("~")
__version__ = "0.1.1rc10"

DEFAULT_JOHNSNOWLABS_VERSION = "5.5.0"
JSL_DOWNLOAD_PACKAGES = os.environ.get("JSL_DOWNLOAD_PACKAGES", True)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PACKAGE_NAME = "ksh-jsl-inference"

DEFAULT_IMAGE_REPOSITORY_NAME = "jsl_inference"

TARGET_PLATFORM = Platform(os.environ.get("PLATFORM", "sagemaker"))

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")

