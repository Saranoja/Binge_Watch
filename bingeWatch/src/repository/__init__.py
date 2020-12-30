"""
Repositories module.

Contains all the logic required to perform CRUD operations on the specific schemas.

Classes:

    TvShowRepository

Functions:

    get_all_shows(object) -> List["TvShow"]
    get_not_snoozed_shows(object) -> List["TvShow"]
    get_last_seen_episode_for_show(object, str) -> Tuple[int, int]
    is_show_in_db(object, str) -> bool
    set_snoozed_for_show(object, str, bool)
    update_score_for_show(object, str, int)
    get_score_for_show(object, str) -> int
    insert_show(object, "TvShow")
    update_last_viewed_episode(object, str, int, int)
    update_last_viewed_date(object, str, str)
"""
from bingeWatch.src.repository.tv_show_repository import TvShowRepository

__all__ = [TvShowRepository]
