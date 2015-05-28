import cherrypy
from models.song import Song
from http.controllers.api_controller import ApiController

class SongController(ApiController):
    def __init__(self):
        self.exposed = True
        self.song    = Song()

    @cherrypy.tools.json_out()
    def GET(self, id = None):
        if id == None:
            return self.song.get_all_songs()
        else:
            try:
                return self.song.get_song_by_id(id)
            except:
                return self.respond_with_404()

    def POST(self, name = None, rtttl = None, wave_form = None):
        data = {
            'name':      str(name),
            'rtttl':     str(rtttl),
            'wave_form': str(wave_form)
        }

        self.song.create_song(data)

    def PUT(self, name = None, rtttl = None, wave_form = None):
        data = {
            'name':      str(name),
            'rtttl':     str(rtttl),
            'wave_form': str(wave_form)
        }

        self.song.update_song_by_id(id, data)

    def DELETE(self, id = None):
        if id == None:
            return self.respond_with_400()
        else:
            try:
                self.song.delete_song_by_id(id)
                return self.respond_with_204()
            except:
                return self.respond_with_404()
