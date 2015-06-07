import os
import cherrypy
from http.api import Api

class Router:
    def __init__(self, database):
        self.api = Api(database)

    @cherrypy.expose
    def index(self):
        return open(os.path.abspath(os.path.join(os.getcwd(), '../client/index.html')), 'rb')

    @cherrypy.expose
    def add(self):
        return open(os.path.abspath(os.path.join(os.getcwd(), '../client/add.html')), 'rb')

    @cherrypy.expose
    def interpret(self):
        return open(os.path.abspath(os.path.join(os.getcwd(), '../client/interpret.html')), 'rb')

    @cherrypy.expose
    def songs(self):
        return open(os.path.abspath(os.path.join(os.getcwd(), '../client/songs.html')), 'rb')

    @cherrypy.expose
    def interpretations(self):
        return open(os.path.abspath(os.path.join(os.getcwd(), '../client/interpretations.html')), 'rb')

    @cherrypy.expose
    def about(self):
        return open(os.path.abspath(os.path.join(os.getcwd(), '../client/about.html')), 'rb')

