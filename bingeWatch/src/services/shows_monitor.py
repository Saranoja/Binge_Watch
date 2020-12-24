from bingeWatch.src.repository.tv_show_repository import TvShowRepository
from bingeWatch.src.services.episodes_retrieval import get_series_episodes


def get_unwatched_episodes(shows_repository: TvShowRepository) -> dict:
    unsnoozed_shows = shows_repository.get_not_snoozed_shows()
    new_episodes = {}
    for show in unsnoozed_shows:
        show_episodes = get_series_episodes(show.name)
        number, season = shows_repository.get_last_seen_episode_for_show(show.name)
        if number and season:
            unseen_episodes = []
            for episode in show_episodes:
                if season <= episode['season'] and number < episode['number']:
                    unseen_episodes.append(episode)
            if unseen_episodes:
                new_episodes[show.name] = unseen_episodes
    return new_episodes
