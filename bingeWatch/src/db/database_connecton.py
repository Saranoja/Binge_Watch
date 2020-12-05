from sqlalchemy import create_engine
import logging

log = logging.getLogger(__name__)


class DatabaseConnection:
    __instance = None

    @staticmethod
    def getInstance():
        if DatabaseConnection.__instance is None:
            DatabaseConnection()
        return DatabaseConnection.__instance

    def __init__(self, user, password, host, port, db):
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
