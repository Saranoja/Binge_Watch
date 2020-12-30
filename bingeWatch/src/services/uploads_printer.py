from typing import List


def print_youtube_uploads(show_name: str, uploads: List[str]) -> None:
    """
    Util function to pretty print youtube uploads for a show.

    :param show_name: name of the tv show
    :param uploads: list of Youtube urls
    :return: None
    """
    print(f'Top {len(uploads)} youtube uploads for {show_name}:')
    for url in uploads:
        print(f'\t{url}')
