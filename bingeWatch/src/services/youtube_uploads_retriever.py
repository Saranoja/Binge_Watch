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
    search_query = f"q={series_name}%20S{episode_season}E{episode_number}"
    url = f"{API_BASE_URL}{API_KEY}&{PART}&{MAX_RESULTS}{max_results}&{search_query}&{CONTENT_TYPE}"
    response = get(url)
    youtube_uploads = loads(response.text)
    youtube_ids = map(
        lambda video: video["id"]["videoId"],
        youtube_uploads["items"])
    youtube_urls = map(lambda id: f'{YOUTUBE_VIDEOS_BASE_URL}{id}', youtube_ids)
    return list(youtube_urls)
