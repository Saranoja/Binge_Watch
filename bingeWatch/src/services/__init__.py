"""
Services module.

Contains services for performing API requests, scraping, formatting responses.

Functions:

    print_episodes(dict)
    get_series_episodes(str)
    update_none_for_score(int) -> int
    get_unwatched_episodes("TvShowRepository") -> Dict[str, List[Dict[str, Any]]]
    get_series_id_from_name(str) -> int
    print_youtube_uploads(str, list)
    get_uploads_for_episode(str, int, int, int) -> List[str]

Misc variables:
    BASE_URL
    ROUTE
    SEARCH_BASE_URL
    API_BASE_URL
    API_KEY
    PART
    MAX_RESULTS
    CONTENT_TYPE
    YOUTUBE_VIDEOS_BASE_URL
"""
