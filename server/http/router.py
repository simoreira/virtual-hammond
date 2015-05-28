import cherrypy
from http.controllers.song_controller import SongController
from http.controllers.interpretation_controller import InterpretationController

class Router:
    def __init__(self):
        self.song           = SongController()
        self.interpretation = InterpretationController()

    def cors(self):
        cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
