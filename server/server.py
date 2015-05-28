#! /usr/bin/python
# encoding=utf-8

import os
import cherrypy
from http.router import Router

def bootstrap():
    api_config = os.path.abspath(os.path.join(os.getcwd(), 'config/api.conf'))
    router = Router()

    cherrypy.tools.CORS = cherrypy.Tool('before_handler', router.cors)
    cherrypy.tree.mount(router, '/api', api_config)

    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == '__main__':
    bootstrap()
