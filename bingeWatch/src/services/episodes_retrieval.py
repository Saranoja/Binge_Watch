import requests
import json
from bingeWatch.src.services.tvmaze_scraper import get_series_id_from_name

BASE_URL = "http://api.tvmaze.com/shows/"
ROUTE = "/episodes"


def get_last_episode(series_name):
    series_id = get_series_id_from_name(series_name)

    url = f"{BASE_URL}{series_id}{ROUTE}"

    response = requests.request("GET", url)

    all_episodes = json.loads(response.text)
    episode_season = all_episodes[len(all_episodes) - 1].get("season")
    episode_number = all_episodes[len(all_episodes) - 1].get("number")
    last_episode = f"S{episode_season}E{episode_number}"

    print(last_episode)


get_last_episode("when they see us")
