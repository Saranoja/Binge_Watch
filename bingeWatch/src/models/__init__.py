"""
Models module.

Contains the application models as database entities, as inheriting a declarative_base.

Classes:

    TvShow

Functions:

    set_last_viewed_episode(object, int)
    set_last_viewed_date(object, str)
    set_score(object, int)
"""
from bingeWatch.src.models.tv_show import TvShow

__all__ = [TvShow]
