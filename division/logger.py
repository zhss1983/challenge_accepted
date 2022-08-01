import logging.config
import logging

from constants import LOGGER_NAME


logging.config.fileConfig("logging.conf")
logger = logging.getLogger(LOGGER_NAME)
