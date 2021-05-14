from tabulate import tabulate


def get_table(log_entries):
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
