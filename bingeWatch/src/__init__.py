""" Source code module. """
from bingeWatch.src.db import DatabaseConnection
from bingeWatch.src.models import TvShow
from bingeWatch.src.repository import TvShowRepository
import logging

logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.INFO)

print("Source init...")

__all__ = [DatabaseConnection, TvShow, TvShowRepository]
