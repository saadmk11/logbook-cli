# `logbook-cli`

Command line tool to keep logs.

**Usage**:

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

## `logbook-cli add`

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

## `logbook-cli delete`

Delete a log entry using it's ID.

**Usage**:

```console
$ logbook-cli delete [OPTIONS] ID
```

**Arguments**:

* `ID`: ID of the log entry  [required]

**Options**:

* `--help`: Show this message and exit.

## `logbook-cli edit`

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

## `logbook-cli find`

List all log entries that match the argument.

**Usage**:

```console
$ logbook-cli find [OPTIONS] DESCRIPTION_CONTAINS
```

**Arguments**:

* `DESCRIPTION_CONTAINS`: String that may match log entry description  [required]

**Options**:

* `--help`: Show this message and exit.

## `logbook-cli list`

List all log entries in a table, limits upto 40 log entries.

**Usage**:

```console
$ logbook-cli list [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `logbook-cli view`

View a single log entry using it's ID.

**Usage**:

```console
$ logbook-cli view [OPTIONS] ID
```

**Arguments**:

* `ID`: ID of the log entry  [required]

**Options**:

* `--help`: Show this message and exit.
