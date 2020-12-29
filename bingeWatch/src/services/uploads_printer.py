def print_youtube_uploads(show_name: str, uploads: list) -> None:
    print(f'Top {len(uploads)} youtube uploads for {show_name}:')
    for url in uploads:
        print(f'\t{url}')
