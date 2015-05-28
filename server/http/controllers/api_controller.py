import cherrypy

class ApiController:
    @cherrypy.tools.json_out()
    def respond_with_404(self):
        return {
            'error': {
                'message': 'Resource not found.',
                'code': 404
            }
        }

    @cherrypy.tools.json_out()
    def respond_with_500(self):
        return {
            'error': {
                'message': 'Server error.',
                'code': 500
            }
        }
