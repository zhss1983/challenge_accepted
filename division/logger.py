import logging.config
import logging


from constants import LOGGER_NAME, LOGGER_CONFIG_FILE


logging.config.fileConfig(LOGGER_CONFIG_FILE)
logger = logging.getLogger(LOGGER_NAME)
