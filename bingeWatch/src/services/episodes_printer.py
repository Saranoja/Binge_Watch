from typing import List, Dict, Any


def print_episodes(series_dict: Dict[str, List[Dict[str, Any]]]) -> None:
    """
    Util function to pretty print episodes given a filtered dictionary.

    :param series_dict: dict which contains titles as keys and the corresponding list of unwatched episodes as values.
    :return: None
    """
    for series_title, episodes in series_dict.items():
        print(f'Show title: {series_title} - Unwatched episodes:')
        for episode in episodes:
            print(f'\tEpisode title: {episode["name"]}')
            print(f'\t\tSeason {episode["season"]}\tNumber {episode["number"]}')
        print()
