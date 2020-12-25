from bingeWatch.src.repository.tv_show_repository import TvShowRepository
from bingeWatch.src.services.shows_monitor import get_unwatched_episodes
from bingeWatch.src.services.json_printer import print_json
from bingeWatch.src.services.youtube_uploads_retriever import get_uploads_for_episode
from bingeWatch.src.services.uploads_printer import print_youtube_uploads
from bingeWatch.src.models.tv_show import TvShow
from sys import exit


def get_user_input(message: str):
    return input(message)


class InteractiveShell():
    def __init__(self, tv_repo: TvShowRepository):
        self.tv_repo = tv_repo
        self.input = ""

    def print_initial(self):
        print("type in one of the following commands:")
        print("\t-show new episodes")
        print("\t-get youtube uploads")
        print("\t-update last seen episode")
        print("\t-add show to the database")
        print("\t-set snoozed flag for show")
        print("\t-update score for show")
        print("\t-exit")
        command = get_user_input("command: ")
        self.solve_command(command)

    def solve_command(self, command: str):
        if command == "show new episodes":
            unwatched_episodes = get_unwatched_episodes(self.tv_repo)
            print_json(unwatched_episodes)
        elif command == "get youtube uploads":
            series_name = get_user_input("type series name: ")
            episode_season = get_user_input("type episode season: ")
            episode_number = get_user_input("type episode number: ")
            uploads_count = get_user_input("type number of results: ")
            resulted_uploads = get_uploads_for_episode(series_name, episode_season, episode_number, uploads_count)
            print_youtube_uploads(series_name, resulted_uploads)
        elif command == "update last seen episode":
            series_name = get_user_input("type series name: ")
            episode_season = get_user_input("type episode season: ")
            episode_number = get_user_input("type episode number: ")
            last_seen_date = get_user_input("last watch date (YYYY-MM-DD): ")
            self.tv_repo.update_last_viewed_episode(series_name, episode_season, episode_number)
            self.tv_repo.update_last_viewed_date(series_name, last_seen_date)
            print("update successful")
        elif command == "add show to the database":
            series_name = get_user_input("type series name: ")
            imdb_link = get_user_input("type imdb link: ")
            is_snoozed = get_user_input("snoozed status: ")
            if is_snoozed.lower() == "true":
                is_snoozed = True
            elif is_snoozed.lower() == "false":
                is_snoozed = False
            new_show = TvShow(series_name, imdb_link, is_snoozed)
            self.tv_repo.insert_show(new_show)
            print("insertion complete")
        elif command == "set snoozed flag for show":
            series_name = get_user_input("type series name: ")
            is_snoozed = get_user_input("update snoozed status to: ")
            if is_snoozed.lower() == "true":
                self.tv_repo.set_snoozed_for_show(series_name, True)
            elif is_snoozed.lower() == "false":
                self.tv_repo.set_snoozed_for_show(series_name, False)
            print("update successful")
        elif command == "update score for show":
            series_name = get_user_input("type series name: ")
            score = get_user_input("update/set score to: ")
            self.tv_repo.update_score_for_show(series_name, score)
            print("update successful")
        elif command == "exit":
            exit()
        else:
            print("unknown command")
            self.print_initial()
