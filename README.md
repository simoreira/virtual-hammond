# Virtual Hammond

## TODO

1. Make list of pip dependencies
2. Make helpers class
3. remove whitespace from rtttl string

## Installation

### Python Dependencies

```shell
$ pip install cherrypy pytest matplotlib
```

### Setup the Database

```shell
$ cd bin
$ chmod +x setup_database.sh
$ ./setup_database.sh
```

### Seed the Database

```shell
$ cd bin
$ chmod +x seed_database.sh
$ ./seed_database.sh
```

## Usage

### Start the Server

```shell
$ cd server
$ python server.py
```

### Run the Client

Browse to `http://127.0.0.1:1337`.

## Tests

Run all the unit tests:

```shell
$ cd bin
$ chmod +x tests.sh
$ ./tests.sh
```
