# Virtual Hammond

Web application that allows users to provide a song's RTTTL specification and a registry, generating the corresponding song.

## Installation

### Python Dependencies

```shell
$ pip install -r requirements.txt
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
