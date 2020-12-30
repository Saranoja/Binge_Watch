from requests import get
from json import loads
from datetime import datetime
from bingeWatch.src import get_series_id_from_name
from typing import List, Dict, Any

BASE_URL = "http://api.tvmaze.com/shows/"
ROUTE = "/episodes"


def get_series_episodes(series_name: str) -> List[Dict[str, Any]]:
    """
    Performs a request to the TvMaze API and gets all the already-aired episodes of a series.

    :param series_name: the name of the tv show
    :return: a filtered list of dictionaries containing the relevant details of each aired episode
    """
    series_id = get_series_id_from_name(series_name)

    url = f"{BASE_URL}{series_id}{ROUTE}"

    response = get(url)

    all_episodes = loads(response.text)

    aired_episodes = [ep for ep in all_episodes if
                      ep['airdate'] != "" and datetime.strptime(ep['airdate'], "%Y-%m-%d") < datetime.today()]

    relevant_fields = ["name", "season", "number", "airdate"]
    relevant_details_dict = [{key: value for key, value in episode.items() if key in relevant_fields} for episode in
                             aired_episodes]

    return relevant_details_dict
