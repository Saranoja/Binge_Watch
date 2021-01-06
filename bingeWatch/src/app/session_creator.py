from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from bingeWatch.src import database_config as config
from bingeWatch.src import DatabaseConnection
import logging


@contextmanager
def session_scope() -> None:
    """Provide a transactional scope around a series of operations."""
    connection = DatabaseConnection.getInstance(config.PGUSER, config.PGPASSWORD, config.PGHOST, config.PGPORT,
                                                config.PGDATABASE)
    engine = connection.engine
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
        session.commit()
    except exc.SQLAlchemyError:
        session.rollback()
        logging.exception("SQLAlchemy Error - Could not create session - Rollback done.")
    finally:
        session.close()
        logging.info("Session closed.")
