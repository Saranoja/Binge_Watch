import requests
from bs4 import BeautifulSoup

SEARCH_BASE_URL = 'https://www.tvmaze.com/search?q='


def get_series_id_from_name(series_name):
    URL = f"{SEARCH_BASE_URL}{series_name}"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    series_id = -1

    for id in soup.find_all('div'):
        if id.get('data-key'):
            series_id = id.get('data-key')
            break

    return series_id
