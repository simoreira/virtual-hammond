import cherrypy
from models.interpretation import Interpretation
from http.controllers.api_controller import ApiController

class InterpretationController(ApiController):
    def __init__(self):
        self.exposed = True
        self.interpretation = Interpretation()

    @cherrypy.tools.json_out()
    def GET(self):
        pass

    def POST(self, name):
        pass

    def PUT(self, id, name):
        pass

    def DELETE(self, id):
        pass
