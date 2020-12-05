from bingeWatch.src.models.tv_show import TV_show


class TV_show_repository:
    def __init__(self, session):
        self.session = session

    def get_all_shows(self) -> list:
        return self.session.query(TV_show).all()

    def insert_show(self, tv_show: TV_show):
        self.session.add(tv_show)
        self.session.commit()

    def update_last_viewed_episode(self, tv_show_id, last_episode):
        self.session.query(TV_show).filter(TV_show.id == tv_show_id).update(
            {TV_show.last_viewed_episode: last_episode}, synchronize_session=False)
        self.session.commit()

    def update_last_viewed_date(self, tv_show_id, last_viewed_date):
        self.session.query(TV_show).filter(TV_show.id == tv_show_id).update(
            {TV_show.last_viewed_date: last_viewed_date},
            synchronize_session=False)
        self.session.commit()
