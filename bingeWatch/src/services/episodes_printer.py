def print_episodes(series_dict: dict):
    for series_title, episodes in series_dict.items():
        print(f'Show title: {series_title} - Unwatched episodes:')
        for episode in episodes:
            print(f'\tEpisode title: {episode["name"]}')
            print(f'\t\tSeason {episode["season"]}\tNumber {episode["number"]}')
        print()
