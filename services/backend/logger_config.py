import logging
from logging.handlers import RotatingFileHandler

# Singleton logger instance


logger = None


def get_logger(name=None):
    global logger
    if logger is None:
        logger = configure_logger()
    if name:
        return logging.getLogger(name)
    return logger


def configure_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
# Log format


    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
# File handler


    file_handler = RotatingFileHandler(
        "logs.log", maxBytes=1024 * 1024, backupCount=10
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
# Add file handler to logger


    logger.addHandler(file_handler)
    return logger
