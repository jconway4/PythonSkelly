import logging
import coloredlogs
from source.utilities.log_formatter import LogFormatter

class Scribbles:
    """
    Namespace class for logging methods.
    """

    def __init__(self, script_name, debug_level, log_path) -> None:
        """
        Initializes logging functions for the active script.

        @param script_name(str): name of the active script
        @param debug_level(str): verbosity of the logs
        @param log_path(str): path to written log file
        @return: none
        """
        
        self.script_name = script_name
        self.debug_level = debug_level
        self.logger = logging.getLogger(script_name)

        if self.logger.handlers:
            self.logger.handlers = []

        log_format = '%(levelname)s %(asctime)s %(message)s'
        log_formatter = LogFormatter(log_format)

        coloredlogs.install(level=debug_level, fmt=log_format)
        self.logger.setLevel(debug_level)

        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(log_formatter)
        file_handler.setLevel(debug_level)
        self.logger.addHandler(file_handler)


    def print_debug(self, message) -> None:
        """
        Prints a debug message.

        @param message(str): message to log
        @return: none
        """

        if self.debug_level != logging.DEBUG:
            return

        self.logger.debug(f'{self.script_name}: {message}')


    def print_warning(self, message) -> None:
        """
        Prints a warning message.

        @param message(str): message to log
        @return: none
        """

        self.logger.warning(f'{self.script_name}: {message}')


    def print_info(self, message) -> None:
        """
        Prints an info message.

        @param message(str): message to log
        @return: none
        """

        self.logger.info(f'{self.script_name}: {message}')


    def print_error(self, message) -> None:
        """
        Prints an error message.

        @param message(str): message to log
        @return: none
        """

        self.error_received = True

        self.logger.error(f'{self.script_name}: {message}')
