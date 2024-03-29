from bingeWatch.src import TvShowRepository, get_series_episodes
from typing import Dict, List, Any


def update_none_for_score(score: int) -> int:
    """
    Util function used for displaying episodes ordered by the score of the tv show.

    :param score: the score to be checked
    :return: value based on whether the score was previously set in the database or not
    """
    if score is None:
        return -10
    else:
        return score


def get_unwatched_episodes(shows_repository: TvShowRepository) -> Dict[str, List[Dict[str, Any]]]:
    """
    :param shows_repository: the repository on which the query will be done
    :return: a dictionary with the tv shows names as keys and the specific lists of unwatched episodes as values
    """
    unsnoozed_shows = shows_repository.get_not_snoozed_shows()
    unsnoozed_shows = sorted(unsnoozed_shows, key=lambda k: update_none_for_score(k.score), reverse=True)
    new_episodes = {}
    for show in unsnoozed_shows:
        show_episodes = get_series_episodes(show.name)
        number, season = shows_repository.get_last_seen_episode_for_show(show.name)
        if number and season:
            unseen_episodes = []
            for episode in show_episodes:
                if season < episode['season'] or (season == episode['season'] and number < episode['number']):
                    unseen_episodes.append(episode)
            if unseen_episodes:
                new_episodes[show.name] = unseen_episodes
    return new_episodes
