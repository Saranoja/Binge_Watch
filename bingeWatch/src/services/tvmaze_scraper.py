from requests import get
from bs4 import BeautifulSoup

SEARCH_BASE_URL = 'https://www.tvmaze.com/search?q='


def get_series_id_from_name(series_name: str) -> int:
    """
    Function that scrapes the TvMaze page in order to get the id for a searched tv show

    :param series_name: name for the tv show to scrape
    :return: TvMaze id for the show
    """
    URL = f"{SEARCH_BASE_URL}{series_name}"
    page = get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    series_id = -1

    for id in soup.find_all('div'):
        if id.get('data-key'):
            series_id = id.get('data-key')
            break

    return series_id
