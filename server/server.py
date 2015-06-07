#! /usr/bin/python
# encoding=utf-8

import os
import cherrypy
import json
from http.router import Router
from database.sqlite_database_manager import SqliteDatabaseManager

def bootstrap():
    api_config = os.path.abspath(os.path.join(os.getcwd(), 'config/server.conf'))
    database_config = json.load(open('config/database.json', 'r'))
    database = SqliteDatabaseManager(database_config['dbname'])
    router = Router(database)
    cherrypy.quickstart(router, '/', api_config)

if __name__ == '__main__':
    bootstrap()
