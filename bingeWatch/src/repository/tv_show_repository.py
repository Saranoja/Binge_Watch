from bingeWatch.src import TvShow
from sqlalchemy import func
from typing import Tuple, List
from sqlalchemy.orm import Session
from sqlalchemy import exc
import logging


class TvShowRepository:
    """
    A class to represent a repository for all the tv shows.

    ...
    Attributes
    ----------
    session:
        database session on which all the transactions will take place

    Methods
    -------
    get_all_shows():
        Returns a list of all the tv shows found in the database.
    get_not_snoozed_shows():
        Returns a list of all the tv shows found in the database which are not snoozed.
    get_last_seen_episode_for_show(show_name):
        Returns the last seen episode given a tv show name.
    is_show_in_db():
        Returns the boolean value specific to whether a tv show is found in the database or not.
    set_snoozed_for_show(show_name, snoozed_value)
        Sets the snoozed value in the database for a certain show.
    update_score_for_show(show_name, score_value)
        Sets the score in the database for a certain show.
    get_score_for_show(show_name):
        Returns the score value from the database for a certain show.
    insert_show(tv_show):
        Inserts a new tv show into the database.
    remove_show(show_name):
        Removes a show from the database.
    update_last_viewed_episode(show_name, last_episode_season, last_episode_number):
        Sets the last viewed episode for a certain tv show in the database.
    update_last_viewed_date(show_name, last_viewed_date):
        Sets the last viewed date for a certain tv show in the database.
    """

    def __init__(self, session: Session):
        """
        Constructs all the necessary attributes for the tv show repository object.

        :param session: database session on which all the transactions will take place
        """
        self.session = session

    def get_all_shows(self) -> List[TvShow]:
        """
        :return: a list of all the tv shows found in the database
        """
        return self.session.query(TvShow).all()

    def get_not_snoozed_shows(self) -> List[TvShow]:
        """
        :return: a list of all the tv shows found in the database which are not snoozed
        """
        return self.session.query(TvShow).filter_by(is_snoozed='False').all()

    def get_last_seen_episode_for_show(self, show_name: str) -> Tuple[int, int]:
        """
        :param show_name: the name of the tv show for which the query will be performed
        :return: the last seen episode given the tv show name
        """
        return self.session.query(TvShow.last_viewed_episode_number, TvShow.last_viewed_episode_season).filter(
            func.lower(TvShow.name) == show_name.lower()).one()

    def is_show_in_db(self, show_name: str) -> bool:
        """
        :param show_name: the name of the tv show for which the query will be performed
        :return: boolean value specific to whether a tv show is found in the database or not
        """
        return self.session.query(TvShow.id).filter(func.lower(TvShow.name) == show_name.lower()).scalar() is not None

    def set_snoozed_for_show(self, show_name: str, snoozed_value: bool) -> None:
        """
        Sets the snoozed value in the database for a certain show.

        :param show_name: the name of the tv show for which the query will be performed
        :param snoozed_value: boolean value for the snooze flag
        :return: None
        """
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).update(
                {TvShow.is_snoozed: snoozed_value}, synchronize_session=False)
            self.session.commit()
            logging.info("Snoozed flag uppdate successful.")
        except exc.SQLAlchemyError:
            self.session.rollback()
            logging.exception("Could not set the snoozed flag. Rollback done.")

    def update_score_for_show(self, show_name: str, score_value: int) -> None:
        """
        Sets the score in the database for a certain show.

        :param show_name: the name of the tv show for which the query will be performed
        :param score_value: number value to mark how good the tv show is
        :return: None
        """
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).update(
                {TvShow.score: score_value}, synchronize_session=False)
            self.session.commit()
            logging.info("Score update successful.")
        except exc.SQLAlchemyError:
            self.session.rollback()
            logging.exception("Could not set the score. Rollback done.")

    def get_score_for_show(self, show_name: str) -> int:
        """
        :param show_name: the name of the tv show for which the query will be performed
        :return: score value from the database for the show
        """
        return self.session.query(TvShow.score).filter(
            func.lower(TvShow.name) == show_name.lower()).one()

    def insert_show(self, tv_show: TvShow) -> None:
        """
        Inserts a new tv show into the database.

        :param tv_show: a tv show object to insert in the database
        :return: None
        """
        try:
            self.session.add(tv_show)
            self.session.commit()
            logging.info(f'Show added successfully.')
        except exc.SQLAlchemyError:
            self.session.rollback()
            logging.exception("Could not add show. Rollback done.")

    def remove_show(self, show_name: str) -> None:
        """
        Removes a show from the database.

        :param show_name: the name of the show to be removed
        :return: None
        """
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).delete(
                synchronize_session=False)
            self.session.commit()
            logging.info("Show removed successfully.")
        except exc.SQLAlchemyError:
            self.session.rollback()
            logging.exception("Could not remove show. Rollback done.")

    def update_last_viewed_episode(self, show_name: str, last_episode_season: int, last_episode_number: int) -> None:
        """
        Sets the last viewed episode for a certain tv show in the database.

        :param show_name: the name of the tv show for which the query will be performed
        :param last_episode_season: number to specify the season number for the last viewed episode
        :param last_episode_number: number to specify the episode number for the last viewed episode
        :return: None
        """
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).update(
                {TvShow.last_viewed_episode_number: last_episode_number}, synchronize_session=False)
            self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).update(
                {TvShow.last_viewed_episode_season: last_episode_season}, synchronize_session=False)
            self.session.commit()
            logging.info("Episode update successful.")
        except exc.SQLAlchemyError:
            self.session.rollback()
            logging.exception("Could not update the last episode. Rollback done.")

    def update_last_viewed_date(self, show_name: str, last_viewed_date: str) -> None:
        """
        Sets the last viewed date for a certain tv show in the database.

        :param show_name: the name of the tv show for which the query will be performed
        :param last_viewed_date: date-like string to specify the date on which the last episode was viewed
        :return: None
        """
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).update(
                {TvShow.last_viewed_date: last_viewed_date},
                synchronize_session=False)
            self.session.commit()
            logging.info("Date update successful.")
        except exc.SQLAlchemyError:
            self.session.rollback()
            logging.exception("Could not update date. Rollback done.")
