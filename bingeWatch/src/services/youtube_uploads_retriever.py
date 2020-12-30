from requests import get
from json import loads
from typing import List

API_BASE_URL = "https://www.googleapis.com/youtube/v3/search?"
API_KEY = "key=AIzaSyBEslP72LahagTyaHAFKqVpv4Lh8fbxyi4"
PART = "part=snippet"
MAX_RESULTS = "maxResults="
CONTENT_TYPE = "type=video"
YOUTUBE_VIDEOS_BASE_URL = "https://www.youtube.com/watch?v="


def get_uploads_for_episode(series_name: str, episode_season: int, episode_number: int, max_results=5) -> List[str]:
    """
    Performs a request to the YouTube API and gets a certain number of video uploads for a tv show.

    :param series_name: the name of the tv show to make the request for
    :param episode_season: the season number for which the request should be done
    :param episode_number: the episode number for which the request should be done
    :param max_results: number of results to be retrieved - default 5
    :return: a list of YouTube URLs to videos related to the specified episode of the tv show
    """
    search_query = f"q={series_name}%20S{episode_season}E{episode_number}"
    url = f"{API_BASE_URL}{API_KEY}&{PART}&{MAX_RESULTS}{max_results}&{search_query}&{CONTENT_TYPE}"
    response = get(url)
    youtube_uploads = loads(response.text)
    youtube_ids = map(
        lambda video: video["id"]["videoId"],
        youtube_uploads["items"])
    youtube_urls = map(lambda id: f'{YOUTUBE_VIDEOS_BASE_URL}{id}', youtube_ids)
    return list(youtube_urls)
