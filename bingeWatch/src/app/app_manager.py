from bingeWatch.src import TV_show
from bingeWatch.src.db import database_config as config
from bingeWatch.src.db.database_connecton import DatabaseConnection
from sqlalchemy.orm import sessionmaker
from bingeWatch.src.repository.tv_show_repository import TV_show_repository
from contextlib import contextmanager


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
        tv_repo = TV_show_repository(current_session)
        for show in tv_repo.get_not_snoozed_shows():
            print(
                f'Show with id {show.id}, name {show.name}, link {show.imdb_link}, is snoozed {show.is_snoozed}')

        # new_show = TV_show(28, "my banana show", "whatever link")
        # new_show.set_last_viewed_episode("S04E23")
        # tv_repo.insert_show(new_show)
        # tv_repo.update_last_viewed_episode(28, "S09E10")
