import requests
import json
from datetime import datetime
from bingeWatch.src.services.tvmaze_scraper import get_series_id_from_name

BASE_URL = "http://api.tvmaze.com/shows/"
ROUTE = "/episodes"


# TODO: map json to contain only episode name, season, number and airdate + filter result to have airdate < current_date

def get_last_episode(series_name):
    series_id = get_series_id_from_name(series_name)

    url = f"{BASE_URL}{series_id}{ROUTE}"

    response = requests.request("GET", url)

    all_episodes = json.loads(response.text)

    aired_episodes = [ep for ep in all_episodes if
                      ep['airdate'] != "" and datetime.strptime(ep['airdate'], "%Y-%m-%d") < datetime.today()]

    relevant_fields = ["name", "season", "number", "airdate"]
    relevant_details_dict = [{key: value for key, value in episode.items() if key in relevant_fields} for episode in
                             aired_episodes]

    return relevant_details_dict
