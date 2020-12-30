from bingeWatch.src import TvShowRepository, InteractiveShell, session_scope

if __name__ == "__main__":
    with session_scope() as current_session:
        tv_repo = TvShowRepository(current_session)
        shell = InteractiveShell(tv_repo)
        while True:
            shell.print_initial()
