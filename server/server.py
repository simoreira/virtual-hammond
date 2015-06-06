#! /usr/bin/python
# encoding=utf-8

import os
import cherrypy
from http.router import Router

def bootstrap():
    # api_config = os.path.abspath(os.path.join(os.getcwd(), 'config/api.conf'))
    router = Router()
    cherrypy.quickstart(router, '/')

if __name__ == '__main__':
    bootstrap()
