from datetime import datetime

import typer

from .managers import LogBookManager
from .utils import get_table


app = typer.Typer()


@app.command()
def list():
    manager = LogBookManager()
    log_entries = manager.list()

    if log_entries:
        typer.echo(get_table(log_entries))
    else:
        typer.echo(
            typer.style(
                f'You do not have any entries in your log book.',
                fg=typer.colors.MAGENTA,
                bold=True
            )
        )


@app.command()
def find(description_contains: str):
    manager = LogBookManager()
    log_entries = manager.find(description_contains)

    if log_entries:
        typer.echo(get_table(log_entries))
    else:
        typer.echo(
            typer.style(
                f'You do not have any entries matching '
                f'"{description_contains}" in your log book.',
                fg=typer.colors.RED,
                bold=True
            )
        )


@app.command()
def view(id: int):
    manager = LogBookManager()
    log_entry = manager.get(id)

    if log_entry:
        log_entry_id = (
            typer.style("Log Entry ID: ", fg=typer.colors.BRIGHT_BLUE, bold=True) +
            str(log_entry.id)
        )
        typer.echo(log_entry_id)

        log_datetime = (
            typer.style("Log Date & Time: ", fg=typer.colors.BRIGHT_BLUE, bold=True) +
            log_entry.log_datetime.strftime("%Y-%m-%d %I:%M %p")
        )
        typer.echo(log_datetime)

        typer.echo(
            typer.style("\nDescription:\n", fg=typer.colors.BRIGHT_BLUE, bold=True)
        )
        typer.echo(log_entry.description + '\n')

        created_at = (
                typer.style("Created at: ", fg=typer.colors.BRIGHT_BLUE, bold=True) +
                log_entry.created_at.strftime("%Y-%m-%d %I:%M %p")
        )
        typer.echo(created_at)

        updated_at = (
                typer.style("Updated at: ", fg=typer.colors.BRIGHT_BLUE, bold=True) +
                log_entry.updated_at.strftime("%Y-%m-%d %I:%M %p")
        )
        typer.echo(updated_at)
    else:
        typer.echo(
            typer.style(
                f'No Log Entry Found with id={id}',
                fg=typer.colors.RED,
                bold=True
            )
        )


@app.command()
def add(
    description: str,
    date: datetime = typer.Option(
        datetime.now().strftime("%Y-%m-%d"), '--date', '-d'
    ),
    time: datetime = typer.Option(
        datetime.now().strftime("%H:%M:%S"), '--time', '-t',
        formats=["%H:%M:%S", "%I:%M %p"]
    )
):
    log_entry_time = time.time()
    log_datetime = datetime.combine(date, log_entry_time)

    manager = LogBookManager()
    created, message = manager.create(description, log_datetime)

    if created:
        typer.echo(
            typer.style(message, fg=typer.colors.GREEN, bold=True)
        )
    else:
        typer.echo(
            typer.style(message, fg=typer.colors.RED, bold=True)
        )


@app.command()
def edit(
    id: int,
    description: str = typer.Option(
        "", '--description'
    ),
    date: datetime = typer.Option(
        None, '--date', '-d'
    ),
    time: datetime = typer.Option(
        None, '--time', '-t',
        formats=["%H:%M:%S", "%I:%M %p"]
    )
):
    log_datetime = None

    if date and time:
        log_entry_time = time.time()
        log_datetime = datetime.combine(date, log_entry_time)

    manager = LogBookManager()
    updated, message = manager.update(
        id,
        description=description,
        log_datetime=log_datetime
    )

    if updated:
        typer.echo(
            typer.style(message, fg=typer.colors.GREEN, bold=True)
        )
    else:
        typer.echo(
            typer.style(message, fg=typer.colors.RED, bold=True)
        )


@app.command()
def delete(id: int):
    manager = LogBookManager()
    deleted, message = manager.delete(id)

    if deleted:
        typer.echo(
            typer.style(message, fg=typer.colors.GREEN, bold=True)
        )
    else:
        typer.echo(
            typer.style(message, fg=typer.colors.RED, bold=True)
        )
