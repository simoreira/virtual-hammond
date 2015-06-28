import os
import cherrypy
from http.api import Api

class Router:
    def __init__(self, database):
        self.api = Api(database)

    def open_file(self, filename):
        return open(os.path.abspath(os.path.join(os.getcwd(), filename)), 'rb')

    @cherrypy.expose
    def default(self, attr):
        return self.open_file('../client/404.html')

    @cherrypy.expose
    def index(self):
        return self.open_file('../client/index.html')

    @cherrypy.expose
    def add(self):
        return self.open_file('../client/add.html')

    @cherrypy.expose
    def songs(self):
        return self.open_file('../client/songs.html')

    @cherrypy.expose
    def about(self):
        return self.open_file('../client/about.html')
