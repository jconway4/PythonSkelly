#!/usr/bin/env python3

import os
import sys
import datetime
from source.base import Base
from source.database.datamancer import Datamancer

run_timestamp = datetime.datetime.now().strftime('%m_%d_%Y_%I_%M%p')
SOURCE_PATH = 'source'

class Runner(Base):
    """
    Entry point for the application.
    """

    def __init__(self) -> None:
        """
        Initializes the runner instance, inheriting from parent class: Base.

        @params: none
        @return: none
        """

        super().__init__()

        sys.path.append(SOURCE_PATH)

        self.main_directory = os.path.dirname(os.path.abspath(__file__))

        self.add_args()
        self.parse_args()

        self.init_logging()

        self.scribbles.print_info(f"Starting new run at {run_timestamp}")
        self.scribbles.print_debug('Verbose logging enabled.')


# Declare this script as our entry point
if __name__ == '__main__':
    runner = Runner()
