import os
import cherrypy
from http.api import Api

class Router:
    def __init__(self):
        self.api = Api()

    @cherrypy.expose
    def index(self):
        return open(os.path.abspath(os.path.join(os.getcwd(), '../client/index.html')), 'rb')

    @cherrypy.expose
    def add(self):
        return open(os.path.abspath(os.path.join(os.getcwd(), '../client/add.html')), 'rb')

    @cherrypy.expose
    def list(self):
        return open(os.path.abspath(os.path.join(os.getcwd(), '../client/list.html')), 'rb')

