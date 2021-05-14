from datetime import datetime

import typer


app = typer.Typer()


@app.command()
def add(
    title: str,
    date: datetime = typer.Option(
        datetime.now().strftime("%Y-%m-%d"), '--date', '-d'
    ),
    time: datetime = typer.Option(
        datetime.now().strftime("%H:%M:%S"), '--time', '-t',
        formats=["%H:%M:%S", "%I:%M %p"]
    )
):
    typer.echo(f'{title}, {date}, {time}')


if __name__ == "__main__":
    app()
