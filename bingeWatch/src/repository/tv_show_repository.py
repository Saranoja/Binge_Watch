from bingeWatch.src.models.tv_show import TvShow
from sqlalchemy import func


class TvShowRepository:
    def __init__(self, session):
        self.session = session

    def get_all_shows(self) -> list:
        return self.session.query(TvShow).all()

    def get_not_snoozed_shows(self) -> list:
        return self.session.query(TvShow).filter_by(is_snoozed='False').all()

    def get_last_seen_episode_for_show(self, show_name):
        return self.session.query(TvShow.last_viewed_episode_number, TvShow.last_viewed_episode_season).filter(
            func.lower(TvShow.name) == show_name.lower()).one()

    def is_show_in_db(self, show_name):
        return self.session.query(TvShow.id).filter(func.lower(TvShow.name) == show_name.lower()).scalar() is not None

    def set_snoozed_for_show(self, show_name, snoozed_value):
        self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).update(
            {TvShow.is_snoozed: snoozed_value}, synchronize_session=False)
        self.session.commit()

    def update_score_for_show(self, show_name, score_value):
        self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).update(
            {TvShow.score: score_value}, synchronize_session=False)
        self.session.commit()

    def get_score_for_show(self, show_name):
        return self.session.query(TvShow.score).filter(
            func.lower(TvShow.name) == show_name.lower()).one()

    def insert_show(self, tv_show: TvShow):
        self.session.add(tv_show)
        self.session.commit()

    def update_last_viewed_episode(self, show_name, last_episode_season, last_episode_number):
        self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).update(
            {TvShow.last_viewed_episode_number: last_episode_number}, synchronize_session=False)
        self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).update(
            {TvShow.last_viewed_episode_season: last_episode_season}, synchronize_session=False)
        self.session.commit()

    def update_last_viewed_date(self, show_name, last_viewed_date):
        self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).update(
            {TvShow.last_viewed_date: last_viewed_date},
            synchronize_session=False)
        self.session.commit()
