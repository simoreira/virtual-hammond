import os
import cherrypy
from http.api_controller import ApiController
from http.client_controller import ClientController

class Router:
    def __init__(self, database):
        self.api    = ApiController(database)
        self.client = ClientController()

    @cherrypy.expose
    def default(self, attr):
        return client.default()

    @cherrypy.expose
    def index(self):
        return client.index()

    @cherrypy.expose
    def add(self):
        return client.add()

    @cherrypy.expose
    def songs(self):
        return client.songs()

    @cherrypy.expose
    def about(self):
        return client.about()
