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
        return self.session.query(TvShow.last_viewed_episode).filter(
            func.lower(TvShow.name) == show_name.lower()).one()

    def set_snoozed_for_show(self, show_name, snoozed_value):
        self.session.query(TvShow).filter(TvShow.name == show_name).update(
            {TvShow.is_snoozed: snoozed_value}, synchronize_session=False)
        self.session.commit()

    def insert_show(self, tv_show: TvShow):
        self.session.add(tv_show)
        self.session.commit()

    def update_last_viewed_episode(self, show_name, last_episode):
        self.session.query(TvShow).filter(TvShow.name == show_name).update(
            {TvShow.last_viewed_episode: last_episode}, synchronize_session=False)
        self.session.commit()

    def update_last_viewed_date(self, show_name, last_viewed_date):
        self.session.query(TvShow).filter(TvShow.name == show_name).update(
            {TvShow.last_viewed_date: last_viewed_date},
            synchronize_session=False)
        self.session.commit()
