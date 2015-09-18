#! /usr/bin/python
# encoding=utf-8

import os
import cherrypy
import json
from helpers import *
from http.router import Router
from database.sqlite_database_manager import SqliteDatabaseManager

if __name__ == '__main__':
    server_config   = abspath_from_relativepath('config/server.conf')
    database_config = json_from_file('config/database.json')

    database = SqliteDatabaseManager(database_config['dbname'])
    router   = Router(database)

    cherrypy.quickstart(router, '/', server_config)
