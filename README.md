# Virtual Hammond

## TODO

1. Make list of pip dependencies
2. Make helpers class
3. remove whitespace from rtttl string

## Installation

### Setup the Database

```
$ cd bin
$ chmod +x setup_database.sh
$ chmod +x seed_database.sh
$ ./setup_database.sh
$ ./seed_database.sh
```

### Start the Server

```
$ cd server
$ python server.py
```

### Run the Client

Browse to http://127.0.0.1:8080

```shell
$ cd client
$ python -m SimpleHTTPServer 1234
```

## Deploy

```
$ cd bin
$ chmod +x deploy.sh
$ ./deploy.sh
```

## Tests

100% unit test coverage.
