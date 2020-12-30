""" Source code module. """
from bingeWatch.src.db import DatabaseConnection, database_config
from bingeWatch.src.models import TvShow
from bingeWatch.src.repository import TvShowRepository
from bingeWatch.src.app.session_creator import session_scope
from bingeWatch.src.services.tvmaze_scraper import get_series_id_from_name
from bingeWatch.src.services.episodes_retriever import get_series_episodes
from bingeWatch.src.services.episodes_printer import print_episodes
from bingeWatch.src.services.youtube_uploads_retriever import get_uploads_for_episode
from bingeWatch.src.services.uploads_printer import print_youtube_uploads
from bingeWatch.src.services.shows_monitor import get_unwatched_episodes
from bingeWatch.src.app.interactive_shell import InteractiveShell
import logging

logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.INFO)

print("Source init...")

__all__ = [DatabaseConnection, TvShow, TvShowRepository, InteractiveShell, session_scope, database_config,
           get_series_id_from_name, get_series_episodes, get_unwatched_episodes, print_episodes,
           get_uploads_for_episode, print_youtube_uploads]
