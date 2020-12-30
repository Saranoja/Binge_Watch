from sqlalchemy import create_engine
from logging import getLogger

log = getLogger(__name__)


class DatabaseConnection:
    """
    A class to represent the database connection, designed as a singleton.

    ...
    Attributes
    ----------
    user: str
        username used to log into the database
    password: str
        password used to log into the database
    host: str
        host on which the database is running
    port: str
        port number on which the database is running
    db: str
        database name

    Methods
    -------
    getInstance(user, password, host, port, db):
        Returns the instance of the database connection class as to preserve the singleton.
    """
    __instance = None

    @staticmethod
    def getInstance(user: str, password: str, host: str, port: str, db: str) -> "DatabaseConnection":
        """
        Returns the instance of the database connection class as to preserve the singleton.

        :param user: username used to log into the database
        :param password: password used to log into the database
        :param host: host on which the database is running
        :param port: port number on which the database is running
        :param db: database name
        :return: an instance of the database connection class
        """
        if DatabaseConnection.__instance is None:
            DatabaseConnection(user, password, host, port, db)
        return DatabaseConnection.__instance

    def __init__(self, user: str, password: str, host: str, port: str, db: str):
        """
        Private. Constructs all the necessary attributes for the database connection object.

        :param user: username used to log into the database
        :param password: password used to log into the database
        :param host: host on which the database is running
        :param port: port number on which the database is running
        :param db: database name
        """
        if DatabaseConnection.__instance is not None:
            raise Exception("Trying to create multiple instances of a singleton")
        else:
            DatabaseConnection.__instance = self
            url = 'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
                user=user, passwd=password, host=host, port=port, db=db)
            try:
                self.engine = create_engine(url, pool_size=50)
                log.info("Connected to PostgreSQL database!")
            except IOError:
                log.exception("Failed to get database connection!")
