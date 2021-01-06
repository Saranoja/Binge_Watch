# Binge Watch

BingeWatch is a tool to monitor the favourite TV shows.
When run, the program will list all episodes that haven't been watched yet, ordered by a specific score the user has previously set.

Another functionality the tool offers is the possibility to search on YouTube for trailers and other uploads that are related to a certain episode of a TV show.

Other possible commands are: snooze a specific show, add or delete one, update its score, update the last seen episode.

Usage: 
```shell script
$ python __main__.py
```

Additional information:

The project makes use of a PostgreSql database, whose credentials can be found and/or adapted in src/db/database_config.py.

The database contains a schema named TV_Shows, whose fields can be found in src/repository/tv_show_repository.py