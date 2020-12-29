from bingeWatch.src.repository.tv_show_repository import TvShowRepository
from bingeWatch.src.services.shows_monitor import get_unwatched_episodes
from bingeWatch.src.services.episodes_printer import print_episodes
from bingeWatch.src.services.youtube_uploads_retriever import get_uploads_for_episode
from bingeWatch.src.services.uploads_printer import print_youtube_uploads
from bingeWatch.src.models.tv_show import TvShow
from sys import exit
from datetime import datetime
import logging


def convert_to_bool(value: str) -> bool:
    if value.lower() == "true":
        return True
    elif value.lower() == "false":
        return False
    else:
        raise ValueError


class InteractiveShell:
    def __init__(self, tv_repo: TvShowRepository):
        self.tv_repo = tv_repo
        self.input = ""

    def read_valid_show_name(self) -> str:
        while True:
            series_name = input("type show name: ")
            if not self.tv_repo.is_show_in_db(series_name):
                logging.error(f'{series_name} show is not in the database yet.')
            else:
                break
        return series_name

    def read_valid_score(self) -> int:
        while True:
            score = input("update/set score to: ")
            val = -1
            try:
                val = int(score)
                if not 0 <= val <= 10:
                    logging.warning("score should be between 0 and 10, but if you think this is a good idea... fine")
                break
            except ValueError:
                logging.error("score should be a number, try again")
                continue
        return val

    def read_valid_date(self) -> str:
        while True:
            date = input("last watch date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, '%Y-%m-%d')
                break
            except ValueError:
                logging.error("date should be YYYY-MM-DD")
                continue
        return date

    def print_initial(self) -> None:
        print("""type in one of the following commands:
                    -show new episodes
                    -get youtube uploads
                    -update last episode
                    -add show
                    -set snoozed flag
                    -update score
                    -exit""")
        command = input("command: ")
        self.solve_command(command)

    def show_new_episodes(self) -> None:
        unwatched_episodes = get_unwatched_episodes(self.tv_repo)
        print_episodes(unwatched_episodes)

    def show_youtube_uploads(self) -> None:
        series_name = input("type show name: ")
        episode_season = input("type episode season: ")
        episode_number = input("type episode number: ")
        uploads_count = input("type number of results: ")
        resulted_uploads = get_uploads_for_episode(series_name, episode_season, episode_number, uploads_count)
        print_youtube_uploads(series_name, resulted_uploads)

    def update_last_episode(self) -> None:
        series_name = self.read_valid_show_name()
        try:
            episode_season = int(input("type episode season: "))
            episode_number = int(input("type episode number: "))
            last_seen_date = self.read_valid_date()
            self.tv_repo.update_last_viewed_episode(series_name, episode_season, episode_number)
            self.tv_repo.update_last_viewed_date(series_name, last_seen_date)
            logging.info("update successful")
        except ValueError:
            logging.error("season and episode should be numbers")

    def add_show(self) -> None:
        series_name = input("type show name: ")
        imdb_link = input("type imdb link: ")
        is_snoozed = convert_to_bool(input("snoozed status: "))
        new_show = TvShow(series_name, imdb_link, is_snoozed)
        self.tv_repo.insert_show(new_show)
        logging.info("insertion complete")

    def set_snoozed_flag(self) -> None:
        series_name = self.read_valid_show_name()
        while True:
            try:
                is_snoozed = convert_to_bool(input("update snoozed status to: "))
                self.tv_repo.set_snoozed_for_show(series_name, is_snoozed)
                logging.info("update successful")
                break
            except ValueError:
                logging.error("value should be boolean")

    def update_score(self) -> None:
        series_name = self.read_valid_show_name()
        score = self.read_valid_score()
        self.tv_repo.update_score_for_show(series_name, score)
        logging.info("update successful")

    def solve_command(self, command: str) -> None:
        valid_commands = ['show new episodes', 'show youtube uploads', 'update last episode',
                          'add show', 'set snoozed flag', 'update score', 'exit']
        command = command.lower()
        if command not in valid_commands:
            logging.error("unknown command")
            self.print_initial()
        else:
            if command == "exit":
                exit()
            function_name = f'self.{command.replace(" ", "_")}()'
            exec(function_name)
