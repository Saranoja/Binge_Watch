from bingeWatch.src.repository.tv_show_repository import TvShowRepository
from bingeWatch.src.services.shows_monitor import get_unwatched_episodes
from bingeWatch.src.services.episodes_printer import print_episodes
from bingeWatch.src.services.youtube_uploads_retriever import get_uploads_for_episode
from bingeWatch.src.services.uploads_printer import print_youtube_uploads
from bingeWatch.src.models.tv_show import TvShow
from sys import exit
from datetime import datetime
import logging


def convert_to_bool(value):
    if value.lower() == "true":
        return True
    elif value.lower() == "false":
        return False


class InteractiveShell:
    def __init__(self, tv_repo: TvShowRepository):
        self.tv_repo = tv_repo
        self.input = ""

    def read_valid_show_name(self):
        while True:
            series_name = input("type show name: ")
            if not self.tv_repo.is_show_in_db(series_name):
                logging.error(f'{series_name} show is not in the database yet.')
            else:
                break
        return series_name

    def read_valid_score(self):
        while True:
            score = input("update/set score to: ")
            val = -1
            try:
                val = int(score)
            except ValueError:
                print("score should be a number, try again")
                continue
            if not 0 <= val <= 10:
                logging.warning("score should be between 0 and 10, but if you think this is a good idea... fine")
                break
        return score

    def read_valid_date(self):
        while True:
            date = input("last watch date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, '%Y-%m-%d')
                break
            except ValueError:
                logging.error("date should be YYYY-MM-DD")
                continue
        return date

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
        print_episodes(unwatched_episodes)

    def get_youtube_uploads(self):
        series_name = input("type show name: ")
        episode_season = input("type episode season: ")
        episode_number = input("type episode number: ")
        uploads_count = input("type number of results: ")
        resulted_uploads = get_uploads_for_episode(series_name, episode_season, episode_number, uploads_count)
        print_youtube_uploads(series_name, resulted_uploads)

    def update_last_episode(self):
        series_name = self.read_valid_show_name()
        episode_season = input("type episode season: ")
        episode_number = input("type episode number: ")
        last_seen_date = self.read_valid_date()
        self.tv_repo.update_last_viewed_episode(series_name, episode_season, episode_number)
        self.tv_repo.update_last_viewed_date(series_name, last_seen_date)
        logging.info("update successful")

    def add_show(self):
        series_name = input("type show name: ")
        imdb_link = input("type imdb link: ")
        is_snoozed = convert_to_bool(input("snoozed status: "))
        new_show = TvShow(series_name, imdb_link, is_snoozed)
        self.tv_repo.insert_show(new_show)
        logging.info("insertion complete")

    def set_snoozed_flag(self):
        series_name = self.read_valid_show_name()
        is_snoozed = convert_to_bool(input("update snoozed status to: "))
        self.tv_repo.set_snoozed_for_show(series_name, is_snoozed)
        logging.info("update successful")

    def update_score(self):
        series_name = self.read_valid_show_name()
        score = self.read_valid_score()
        self.tv_repo.update_score_for_show(series_name, score)
        logging.info("update successful")

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
            logging.error("unknown command")
            self.print_initial()
