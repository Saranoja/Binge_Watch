from bingeWatch.src.models.tv_show import TV_show
from sqlalchemy import func


class TV_show_repository:
    def __init__(self, session):
        self.session = session

    def get_all_shows(self) -> list:
        return self.session.query(TV_show).all()

    def get_not_snoozed_shows(self) -> list:
        return self.session.query(TV_show).filter_by(is_snoozed='False').all()

    def get_last_seen_episode_for_show(self, show_name):
        return self.session.query(TV_show.last_viewed_episode).filter(
            func.lower(TV_show.name) == show_name.lower()).one()

    def set_snoozed_for_show(self, show_name, snoozed_value):
        self.session.query(TV_show).filter(TV_show.name == show_name).update(
            {TV_show.is_snoozed: snoozed_value}, synchronize_session=False)
        self.session.commit()

    def insert_show(self, tv_show: TV_show):
        self.session.add(tv_show)
        self.session.commit()

    def update_last_viewed_episode(self, show_name, last_episode):
        self.session.query(TV_show).filter(TV_show.name == show_name).update(
            {TV_show.last_viewed_episode: last_episode}, synchronize_session=False)
        self.session.commit()

    def update_last_viewed_date(self, show_name, last_viewed_date):
        self.session.query(TV_show).filter(TV_show.name == show_name).update(
            {TV_show.last_viewed_date: last_viewed_date},
            synchronize_session=False)
        self.session.commit()
