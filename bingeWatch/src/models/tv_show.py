from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TV_show(Base):
    __tablename__ = "TV_Shows"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False)
    imdb_link = Column("imdb_link", String, nullable=False)
    last_viewed_episode = Column("last_viewed_episode", String)
    last_viewed_date = Column("last_viewed_date", Date)
    score = Column("score", Integer)
    is_snoozed = Column("is_snoozed", Boolean, nullable=False)

    def __init__(self, id, name, imdb_link, is_snoozed=False):
        self.id = id
        self.name = name
        self.imdb_link = imdb_link
        self.last_viewed_episode = None
        self.last_viewed_date = None
        self.score = None
        self.is_snoozed = is_snoozed

    def set_last_viewed_episode(self, last_viewed_episode):
        self.last_viewed_episode = last_viewed_episode

    def set_last_viewed_date(self, last_viewed_date):
        self.last_viewed_date = last_viewed_date

    def set_score(self, score):
        self.score = score
