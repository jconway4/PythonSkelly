import configparser
from peewee import Proxy, Database, Model
from time import sleep
from source.base import Base
from source.database.models import *

class Datamancer(Base):
    """
    Flexible database manipulator. Can be built for any SQL/NoSQL database.
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the Datamancer class. A Peewee disciple.
        This should be done for every connection to the database.

        @params: none
        @return: none
        """

        super().__init__()        
        
        self.add_args()
        self.parse_args()
        
        self.init_logging()

        # define database/proxy
        self.database_proxy = Proxy()
        self.database = self.get_database()

        # init database/proxy
        self.database_proxy.initialize(self.database)
        #self.database.connect()

        #create tables here
        

    def get_database(self) -> Database:
        """
        Returns a database, parsed from the config file and env variables.

        @params: none
        @return (Database): a database instance to be used by peewee
        """
        
        config_parser = configparser.ConfigParser()        
        config_parser.read('app.config')

        db_type = os.environ.get('SERVER_TYPE', 'Local')

        if db_type == 'Local':
                database_name = 'database'
                
                # database = 
        else:
            database_name = config_parser[f'Database{db_type}'].get('name', None)
            db_port = config_parser[f'Database{db_type}'].get('port', 3306)
            db_user = config_parser[f'Database{db_type}'].get('user', None)
            db_password = config_parser[f'Database{db_type}'].get('password', None)
            db_host = config_parser[f'Database{db_type}'].get('host', None)
            
            # database =

            
        # return database
