![Logbook-cli-banner](https://user-images.githubusercontent.com/24854406/118286755-9fbe4980-b4f4-11eb-8c53-1af215343e8e.png)

# logbook-cli

Keep Your Daily Events Recorded Using Command Line.


## How Does It Work?

`logbook-cli` is created using python. It uses `typer` for the Command Line Interface
and `SQLAlchemy` to interact with the database (`sqlite`).
All the log entries are stored into the `sqlite` database.


## Installation

You can install `logbook-cli` by using `pip`:

```console
pip install logbook-cli
```


## Configuration

`logbook-cli` stores the `sqlite` database in `~/.logbook/` directory by default.

You can use `LOG_BOOK_DATABASE_URL` environment variable to use a different location.

**Example:**

```console
export LOG_BOOK_DATABASE_URL=sqlite:///logbook.sqlite3
```


## How to use `logbook-cli`

**Usage**

```console
$ logbook-cli [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `add`: Add a log entry to the logbook.
* `delete`: Delete a log entry using it's ID.
* `edit`: Update a log entry using it's ID.
* `find`: List all log entries that match the argument.
* `list`: List all log entries in a table, limits upto...
* `view`: View a single log entry using it's ID.

### `logbook-cli add`

Add a log entry to the logbook.

**Usage**:

```console
$ logbook-cli add [OPTIONS] DESCRIPTION
```

**Arguments**:

* `DESCRIPTION`: Description of the log entry  [required]

**Options**:

* `-d, --date [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: Date of the log entry  [default: **log entry date**]
* `-t, --time [%H:%M:%S|%I:%M %p]`: Time of the log entry  [default: **log entry time**]
* `--help`: Show this message and exit.

**Example:**

```console
$ logbook-cli add -d "2021-05-10" -t "10:00 PM" "This is a Test Log Entry"
```

### `logbook-cli delete`

Delete a log entry using it's ID.

**Usage**:

```console
$ logbook-cli delete [OPTIONS] ID
```

**Arguments**:

* `ID`: ID of the log entry  [required]

**Options**:

* `--help`: Show this message and exit.

**Example:**

```console
$ logbook-cli delete 1
```

### `logbook-cli edit`

Update a log entry using it's ID.

**Usage**:

```console
$ logbook-cli edit [OPTIONS] ID
```

**Arguments**:

* `ID`: ID of the log entry  [required]

**Options**:

* `--description TEXT`: New Description for the log entry  [default: ]
* `-d, --date [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]`: New Date for the log entry
* `-t, --time [%H:%M:%S|%I:%M %p]`: New Time for the log entry
* `--help`: Show this message and exit.

**Example:**

```console
$ logbook-cli edit 1 -d "2021-05-10" -t "10:00 PM" --description "This is a Edited Test Log Entry"
```

### `logbook-cli find`

List all log entries that match the argument.

**Usage**:

```console
$ logbook-cli find [OPTIONS] DESCRIPTION_CONTAINS
```

**Arguments**:

* `DESCRIPTION_CONTAINS`: String that may match log entry description  [required]

**Options**:

* `--help`: Show this message and exit.

**Example:**

```console
$ logbook-cli find "test"
```

### `logbook-cli list`

List all log entries in a table, limits upto 40 log entries.

**Usage**:

```console
$ logbook-cli list [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

**Example:**

```console
$ logbook-cli list
```

### `logbook-cli view`

View a single log entry using it's ID.

**Usage**:

```console
$ logbook-cli view [OPTIONS] ID
```

**Arguments**:

* `ID`: ID of the log entry  [required]

**Options**:

* `--help`: Show this message and exit.

**Example:**

```console
$ logbook-cli view 1
```

## Screenshot

![logbook-cli-screenshot](https://user-images.githubusercontent.com/24854406/118287484-4dc9f380-b4f5-11eb-8e2a-e6bf0bf35942.png)

