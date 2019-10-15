import os
import sys
import datetime
import logging
import configparser
from time import sleep
from argparse import ArgumentParser
from source.utilities.scribbles import Scribbles
from source.utilities.sys_utils import Utilities

class Base:
    """
    Cornerstone class for the application.
    """
    
    init_timestamp = datetime.datetime.now().strftime('%m_%d_%Y_%I_%M%p')

    #logging variables
    logs_main_directory = 'logs'
    logs_directory = f"{logs_main_directory}/{init_timestamp}"
    log_file_name = None # override ex: script_1.log

    # etc
    error_received = None # override ex: True if error is reported


    def __init__(self) -> None:
        """
        Initializes an instance of the Base class.

        @params: none
        @return: none
        """

        self.script_name = os.path.basename(sys.modules[self.__module__].__file__)
        self.utilities = Utilities()
        self.argparser = ArgumentParser()

        self.init_config()
        self.create_directories()


    def add_args(self) -> None:
        """
        Processes and passes arguments.

        @params: none
        @return: none
        """

        self.argparser.add_argument('--run',
                                    action='store_true', default=False,
                                    help='run the application')

        self.argparser.add_argument('--verbose',
                                 action="store_true", default=False,
                                 help="adds debug statements to logs")


    def parse_args(self) -> None:
        """
        Parses passed arguments.

        @params: none
        @return: none
        """

        self.args, unknown = self.argparser.parse_known_args()

        if len(sys.argv) <= 1:
            self.argparser.print_help()
            quit()


    def init_config(self) -> None:
        """
        Initializes the config file settings.

        @params: none
        @return: none
        """

        self.config_parser = configparser.ConfigParser()
        self.config_parser.read('app.config')

        # General
        self.app_name = self.config_parser['General'].get('app_name', 'Unknown')


    def init_logging(self) -> None:
        """
        Initializes logging functions for this Base class or child.
        Logs will be named after the running script.

        @params: none
        @return: none
        """

        self.debug_level = logging.INFO

        if self.args.verbose:
            self.debug_level = logging.DEBUG

        self.log_filename = f"{self.utilities.basename_of(path=self.script_name)}.log"
        self.log_path = f"{self.logs_directory}/{self.log_filename}"

        #INIT scribbles
        self.scribbles = Scribbles(self.script_name, self.debug_level, self.log_path)


    def create_directories(self) -> None:
        """
        Creates any directories needed by the app, or this specific run.

        @params: none
        @return: none
        """

        self.utilities.create_directory(self.logs_directory)
