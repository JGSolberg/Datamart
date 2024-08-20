import logging.config
import os

def setup_logging(log_name, write_logs):
    """
    Configures logging based on the provided parameters.

    Args:
        log_name (str): The name of the log file to write to.
        write_logs (bool): Flag indicating whether to write logs to a file.
    """
    log_file_path = os.path.join(os.path.dirname(__file__), 'logging_config.ini')
    
    logging.config.fileConfig(log_file_path, disable_existing_loggers=False)

    if write_logs:
        log_filename = os.path.join(os.getenv('LOG_PATH', '_logs'), f'{log_name}.log')
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)')
        file_handler.setFormatter(formatter)
        logging.getLogger().addHandler(file_handler)
