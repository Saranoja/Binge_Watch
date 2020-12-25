from bingeWatch.src.repository.tv_show_repository import TvShowRepository
from bingeWatch.src.services.shows_monitor import get_unwatched_episodes
from bingeWatch.src.services.json_printer import print_json
from bingeWatch.src.services.youtube_uploads_retriever import get_uploads_for_episode
from bingeWatch.src.services.uploads_printer import print_youtube_uploads
from bingeWatch.src.models.tv_show import TvShow
from sys import exit


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
        command = input("command: ")
        self.solve_command(command)

    def show_new_episodes(self):
        unwatched_episodes = get_unwatched_episodes(self.tv_repo)
        print_json(unwatched_episodes)

    def get_youtube_uploads(self):
        series_name = input("type series name: ")
        episode_season = input("type episode season: ")
        episode_number = input("type episode number: ")
        uploads_count = input("type number of results: ")
        resulted_uploads = get_uploads_for_episode(series_name, episode_season, episode_number, uploads_count)
        print_youtube_uploads(series_name, resulted_uploads)

    def update_last_episode(self):
        series_name = input("type series name: ")
        episode_season = input("type episode season: ")
        episode_number = input("type episode number: ")
        last_seen_date = input("last watch date (YYYY-MM-DD): ")
        self.tv_repo.update_last_viewed_episode(series_name, episode_season, episode_number)
        self.tv_repo.update_last_viewed_date(series_name, last_seen_date)
        print("update successful")

    def add_show(self):
        series_name = input("type series name: ")
        imdb_link = input("type imdb link: ")
        is_snoozed = input("snoozed status: ")
        if is_snoozed.lower() == "true":
            is_snoozed = True
        elif is_snoozed.lower() == "false":
            is_snoozed = False
        new_show = TvShow(series_name, imdb_link, is_snoozed)
        self.tv_repo.insert_show(new_show)
        print("insertion complete")

    def set_snoozed_flag(self):
        series_name = input("type series name: ")
        is_snoozed = input("update snoozed status to: ")
        if is_snoozed.lower() == "true":
            self.tv_repo.set_snoozed_for_show(series_name, True)
        elif is_snoozed.lower() == "false":
            self.tv_repo.set_snoozed_for_show(series_name, False)
        print("update successful")

    def update_score(self):
        series_name = input("type series name: ")
        score = input("update/set score to: ")
        self.tv_repo.update_score_for_show(series_name, score)
        print("update successful")

    def solve_command(self, command: str):
        if command == "show new episodes":
            self.show_new_episodes()
        elif command == "get youtube uploads":
            self.get_youtube_uploads()
        elif command == "update last seen episode":
            self.update_last_episode()
        elif command == "add show to the database":
            self.add_show()
        elif command == "set snoozed flag for show":
            self.set_snoozed_flag()
        elif command == "update score for show":
            self.update_score()
        elif command == "exit":
            exit()
        else:
            print("unknown command")
            self.print_initial()
