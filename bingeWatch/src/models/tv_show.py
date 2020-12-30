from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TvShow(Base):
    """
    A class to represent a tv show.

    ...
    Attributes
    ----------
    name: str
        name of the tv show
    imdb_link: str
        imdb link for the show
    is_snoozed: str
        flag to mark whether the show is on snooze or not
    last_viewed_episode: int
        the last viewed episode by the user
    last_viewed_date: str
        the date on which the last episode was viewed
    score: int
        a value to mark how good the show is

    Methods
    -------
    set_last_viewed_episode(last_viewed_episode):
        Sets the last viewed episode of the tv show.
    set_last_viewed_date(last_viewed_date):
        Sets the date on which the last episode of the tv show was viewed.
    set_score(score):
        Sets the score for the tv show.
    """
    __tablename__ = "TV_Shows"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    imdb_link = Column("imdb_link", String, nullable=False)
    last_viewed_episode_number = Column("last_viewed_episode_number", Integer)
    last_viewed_episode_season = Column("last_viewed_episode_season", Integer)
    last_viewed_date = Column("last_viewed_date", Date)
    score = Column("score", Integer)
    is_snoozed = Column("is_snoozed", Boolean, nullable=False)

    def __init__(self, name: str, imdb_link: str, is_snoozed=False):
        self.name = name
        self.imdb_link = imdb_link
        self.last_viewed_episode = None
        self.last_viewed_date = None
        self.score = None
        self.is_snoozed = is_snoozed

    def set_last_viewed_episode(self, last_viewed_episode: int) -> None:
        """
        Sets the last viewed episode of the tv show.

        :param last_viewed_episode:
        :return: None
        """
        self.last_viewed_episode = last_viewed_episode

    def set_last_viewed_date(self, last_viewed_date: str) -> None:
        """
        Sets the date on which the last episode of the tv show was viewed.

        :param last_viewed_date:
        :return: None
        """
        self.last_viewed_date = last_viewed_date

    def set_score(self, score: int) -> None:
        """
        Sets the score for the tv show.

        :param score:
        :return: None
        """
        self.score = score
