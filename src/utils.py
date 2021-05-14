import os
from pathlib import Path

from tabulate import tabulate


def get_table(log_entries):
    """Create table for Log Entries using tabulate"""
    table_data = [
        [
            entry.id,
            entry.description[0:30],
            entry.log_datetime.strftime("%Y-%m-%d %I:%M %p"),
            entry.created_at.strftime("%Y-%m-%d %I:%M %p"),
            entry.updated_at.strftime("%Y-%m-%d %I:%M %p")
        ]
        for entry in log_entries
    ]

    table_headers = [
        "# ID",
        "description",
        "Log Datetime",
        "Created At",
        "Updated At"
    ]

    return tabulate(
        table_data,
        headers=table_headers,
        tablefmt="pretty"
    )


def get_database_url():
    """Get Database URL from environment variable or "~/.logbook/" directory"""
    LOG_BOOK_DATABASE_URL = os.environ.get('LOG_BOOK_DATABASE_URL')

    if LOG_BOOK_DATABASE_URL:
        return LOG_BOOK_DATABASE_URL

    database_directory = str(Path.home() / '.logbook')

    # create "~/.logbook/" directory if it does not exist
    Path(database_directory).mkdir(parents=True, exist_ok=True)

    return 'sqlite:///' + database_directory + '/logbook.sqlite3'
