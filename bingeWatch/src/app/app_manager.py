from bingeWatch.src.db import database_config as config
from bingeWatch.src.db.database_connecton import DatabaseConnection
from sqlalchemy.orm import sessionmaker
from bingeWatch.src.repository.tv_show_repository import TvShowRepository
from contextlib import contextmanager
from bingeWatch.src.services.shows_monitor import get_unwatched_episodes
from json import dumps


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":
    connection = DatabaseConnection(config.PGUSER, config.PGPASSWORD, config.PGHOST, config.PGPORT, config.PGDATABASE)
    engine = connection.engine
    with session_scope() as current_session:
        tv_repo = TvShowRepository(current_session)
        unwatched_episodes = dumps(get_unwatched_episodes(tv_repo), indent=2)
        print(unwatched_episodes)
