# Virtual Hammond

## TODO

1. `effects` or `effect` in the interpretations table?
2. Is it enough to UTF-8 and shebang the main `server.py` file?
3. Extend `object` in all classes.

## Installation

### Setup the Database

```
$ cd bin
$ chmod +x setup_database.sh
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
