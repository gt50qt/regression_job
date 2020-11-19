from nb_log import LogManager
from nb_log_config import LOG_PATH

logger = LogManager(logger_name="api").get_logger_and_add_handlers(is_add_stream_handler=True,
                                                                   log_filename="api.log",
                                                                   log_path=LOG_PATH)

logger.debug("----debug--------")
logger.info("-------info-------")
logger.warning("-----waring----")
logger.error("----error----")
print("hello")