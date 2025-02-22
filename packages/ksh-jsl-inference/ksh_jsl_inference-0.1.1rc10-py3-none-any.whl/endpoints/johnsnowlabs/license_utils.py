import os
import base64
from johnsnowlabs.nlp import settings
import json
import time

from endpoints import JslInferenceException


def is_license_valid(license_file) -> bool:
    """
    Check if the license file is valid

    :param str license_file: The path to the license file
    :raises FileNotFoundError: If the license file does not exist
    :raises JslInferenceException: If the license is invalid
    :return: True if the license is valid, False otherwise
    """
    if not os.path.isfile(license_file):
        raise FileNotFoundError(f"Provided license file does not exist: {license_file}")

    try:
        with open(license_file, "r") as f:
            content = f.read()
            license_content = json.loads(content)
            license = (
                license_content.get("HC_LICENSE")
                or license_content.get("OCR_LICENSE")
                or license_content.get("SPARK_NLP_LICENSE")
                or license_content.get("SPARK_OCR_LICENSE")
            )

            token_payload = license.split(".")[1]
            token_payload_decoded = str(base64.b64decode(token_payload + "=="), "utf-8")
            payload = json.loads(token_payload_decoded)
            # Make sure license is active
            is_active = time.time() < payload.get("exp")
            # Make sure license has atleast healthcare scopes
            has_inference_scope = "healthcare:inference" in payload.get("scope")
            return is_active and has_inference_scope
    except Exception:
        raise JslInferenceException("Invalid JSL License")


def find_license_from_jsl_home():
    """Find the active license file in the JSL license directory
    :raises Exception: If no active license is found
    """
    source_path = settings.license_dir
    """ List all json files in the license directory """
    license_files = [
        os.path.join(source_path, f)
        for f in os.listdir(source_path)
        if (f.endswith(".json") and not f.startswith("info.json"))
    ]

    try:
        return next(file for file in license_files if is_license_valid(file))
    except Exception:
        raise JslInferenceException("Active JSL License Required")
