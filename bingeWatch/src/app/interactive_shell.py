from bingeWatch.src import TvShowRepository, TvShow
from bingeWatch.src import get_unwatched_episodes, print_episodes, get_uploads_for_episode, print_youtube_uploads
from sys import exit
from datetime import datetime
import logging


def convert_to_bool(value: str) -> bool:
    """
    Transforms a string value into a boolean one, if possible.

    :param value: value to be converted to bool
    :return: corresponding boolean value
    """
    if value.lower() == "true":
        return True
    elif value.lower() == "false":
        return False
    else:
        raise ValueError


class InteractiveShell:
    """
    A class to represent the shell in which the user can type commands.

    ...
    Attributes
    ----------
    tv_repo: TvShowRepository
        a tv shows repository object on which CRUD operations shall be performed

    Methods
    ----------
        read_valid_show_name()
            Reads from the console tv show names until a valid one is read.
        read_valid_score()
            Reads from the console score values until a valid one is read.
        read_valid_date()
            Reads from the console date values until a valid one is read.
        print_initial()
            Prints available commands.
        show_new_episodes()
            Displays the episodes which have not been marked as viewed by the user and are not snoozed.
        show_youtube_uploads()
            Displays Youtube video uploads with regard to a certain episode of any tv show.
        update_last_episode()
            Updates the last viewed episode of a tv show in the database.
        add_show()
            Adds a new show in the database.
        set_snoozed_flag()
            Sets the snoozed flag for a certain tv show.
        update_score()
            Sets the score for a certain tv show.
        solve_command(command)
            Executes the command given by the user in the console.
    """

    def __init__(self, tv_repo: TvShowRepository):
        """
        Constructs all the necessary attributes for the interactive shell object.

        :param tv_repo: a tv shows repository object on which CRUD operations shall be performed
        """
        self.tv_repo = tv_repo

    def read_valid_show_name(self) -> str:
        """
        Reads from the console tv show names until a valid one is read.

        :return: first show name that is read from the console and found in the database
        """
        while True:
            series_name = input("type show name: ")
            if not self.tv_repo.is_show_in_db(series_name):
                logging.error(f'{series_name} show is not in the database yet.')
            else:
                break
        return series_name

    def read_valid_score(self) -> int:
        """
        Reads from the console score values until a valid one is read.

        :return: first score value that is read from the console and is an int
        """
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
        """
        Reads from the console date values until a valid one is read.

        :return: first date value that is read from the console and respects the format "YYYY-MM-DD"
        """
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
        """
        Prints available commands.

        :return: None
        """
        print("""type in one of the following commands:
                    -show new episodes
                    -show youtube uploads
                    -update last episode
                    -add show
                    -set snoozed flag
                    -update score
                    -exit""")
        command = input("command: ")
        self.solve_command(command)

    def show_new_episodes(self) -> None:
        """
        Displays the episodes which have not been marked as viewed by the user and are not snoozed.

        :return: None
        """
        unwatched_episodes = get_unwatched_episodes(self.tv_repo)
        print_episodes(unwatched_episodes)

    def show_youtube_uploads(self) -> None:
        """
        Displays Youtube video uploads with regard to a certain episode of any tv show.

        :return: None
        """
        series_name = input("type show name: ")
        while True:
            try:
                episode_season = int(input("type episode season: "))
                episode_number = int(input("type episode number: "))
                uploads_count = int(input("type number of results: "))
                resulted_uploads = get_uploads_for_episode(series_name, episode_season, episode_number, uploads_count)
                print_youtube_uploads(series_name, resulted_uploads)
                break
            except ValueError:
                logging.error("these values should be numbers")

    def update_last_episode(self) -> None:
        """
        Updates the last viewed episode of a tv show in the database.

        :return: None
        """
        series_name = self.read_valid_show_name()
        while True:
            try:
                episode_season = int(input("type episode season: "))
                episode_number = int(input("type episode number: "))
                last_seen_date = self.read_valid_date()
                self.tv_repo.update_last_viewed_episode(series_name, episode_season, episode_number)
                self.tv_repo.update_last_viewed_date(series_name, last_seen_date)
                logging.info("update successful")
                break
            except ValueError:
                logging.error("season and episode should be numbers")

    def add_show(self) -> None:
        """
        Adds a new show in the database.

        :return: None
        """
        series_name = input("type show name: ")
        imdb_link = input("type imdb link: ")
        is_snoozed = convert_to_bool(input("snoozed status: "))
        new_show = TvShow(series_name, imdb_link, is_snoozed)
        self.tv_repo.insert_show(new_show)
        logging.info("insertion complete")

    def set_snoozed_flag(self) -> None:
        """
        Sets the snoozed flag for a certain tv show.

        :return: None
        """
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
        """
        Sets the score for a certain tv show.

        :return: None
        """
        series_name = self.read_valid_show_name()
        score = self.read_valid_score()
        self.tv_repo.update_score_for_show(series_name, score)
        logging.info("update successful")

    def solve_command(self, command: str) -> None:
        """
        Executes the command given by the user in the console.
        :param command: the command the user types in the console
        :return: None
        """
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
