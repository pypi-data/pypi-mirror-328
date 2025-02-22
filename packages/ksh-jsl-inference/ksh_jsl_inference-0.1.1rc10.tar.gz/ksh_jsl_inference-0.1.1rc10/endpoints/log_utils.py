import logging
import os


logger = logging.getLogger(__name__.split(".")[0])
logger.addHandler(logging.NullHandler())


def configure_logging():
    log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(level=logging.WARN)
    logger.setLevel(log_level)
