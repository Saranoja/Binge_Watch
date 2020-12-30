"""
Database module of the application.

Contains the logic and configuration for connecting to a PostgreSQL database.

Classes:

    DatabaseConnection

Functions:

    getInstance(str, str, str, str) -> "DatabaseConnection"

Misc variables:

    PGHOST
    PGUSER
    PGPASSWORD
    PGPORT
    PGDATABASE
"""
from bingeWatch.src.db.database_connecton import DatabaseConnection

__all__ = [DatabaseConnection]
