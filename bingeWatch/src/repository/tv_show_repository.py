from bingeWatch.src import TvShow
from sqlalchemy import func
from typing import Tuple, List


class TvShowRepository:
    def __init__(self, session):
        self.session = session

    def get_all_shows(self) -> List[TvShow]:
        return self.session.query(TvShow).all()

    def get_not_snoozed_shows(self) -> List[TvShow]:
        return self.session.query(TvShow).filter_by(is_snoozed='False').all()

    def get_last_seen_episode_for_show(self, show_name: str) -> Tuple[int, int]:
        return self.session.query(TvShow.last_viewed_episode_number, TvShow.last_viewed_episode_season).filter(
            func.lower(TvShow.name) == show_name.lower()).one()

    def is_show_in_db(self, show_name: str) -> bool:
        return self.session.query(TvShow.id).filter(func.lower(TvShow.name) == show_name.lower()).scalar() is not None

    def set_snoozed_for_show(self, show_name: str, snoozed_value: bool):
        self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).update(
            {TvShow.is_snoozed: snoozed_value}, synchronize_session=False)
        self.session.commit()

    def update_score_for_show(self, show_name: str, score_value: int):
        self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).update(
            {TvShow.score: score_value}, synchronize_session=False)
        self.session.commit()

    def get_score_for_show(self, show_name: str) -> int:
        return self.session.query(TvShow.score).filter(
            func.lower(TvShow.name) == show_name.lower()).one()

    def insert_show(self, tv_show: TvShow) -> None:
        self.session.add(tv_show)
        self.session.commit()

    def update_last_viewed_episode(self, show_name: str, last_episode_season: int, last_episode_number: int):
        self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).update(
            {TvShow.last_viewed_episode_number: last_episode_number}, synchronize_session=False)
        self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).update(
            {TvShow.last_viewed_episode_season: last_episode_season}, synchronize_session=False)
        self.session.commit()

    def update_last_viewed_date(self, show_name: str, last_viewed_date: str):
        self.session.query(TvShow).filter(func.lower(TvShow.name) == show_name.lower()).update(
            {TvShow.last_viewed_date: last_viewed_date},
            synchronize_session=False)
        self.session.commit()
