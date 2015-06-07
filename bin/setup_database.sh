#! /usr/bin/env bash

set -e

#############################################################################
### HELPERS
#############################################################################

msg() {
    echo "$1"
    sleep 0.1
}

#############################################################################
### CONFIGURATION
#############################################################################

db="hammond.sqlite3"

#############################################################################
### MAIN
#############################################################################

main() {
    msg ">>> Changing into database directory..."

    cd "../server/database"
    msg "  Changed into database directory."

    msg ">>> Deleting old database..."

    rm -rf "$db"
    msg "  Old database deleted."

    msg ">>> Creating database..."

    sqlite3 "$db" ".exit"
    msg "  Database created."

    msg ">>> Running migrations..."

    for file in $(find ./migrations -name '*.sql'); do
        cat $file | sqlite3 "$db"
        msg "  Ran migration $file."
    done
}

#############################################################################
### BOOTSTRAP
#############################################################################

main "$@"
