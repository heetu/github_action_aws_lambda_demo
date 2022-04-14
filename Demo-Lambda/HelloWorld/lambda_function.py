# This function is created to print hello-world
import logging.config
import logging.config

# Logging Configuration
from loggerfile import log_debug, log_info, log_error

logging.config.fileConfig('config.ini')

def lambda_handler(event: dict, context: object) -> None:
    try:
        log_info("Hello World")
        return "Hello World"
    except Exception as e:
        log_error("ERROR:{}".format(e))