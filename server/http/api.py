import cherrypy
import hashlib
from models.song import Song
from models.interpretation import Interpretation
from image.waveform_image_renderer import WaveformImageRenderer
from sound.wav_generator import WavGenerator
from sound.rtttl_parser import RtttlParser

class Api(object):
    def __init__(self, database):
        self.song           = Song(database)
        self.interpretation = Interpretation(database)

    def md5(self, string):
        return hashlib.md5(string).hexdigest()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return self.respond_failure('The API root has no resources.')

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def create_song(self, rtttl):
        try:
            if len(rtttl) == 0:
                raise Exception('Empty RTTTL string.')

            data = {
                'rtttl': str(rtttl)
            }

            data = self.song.create_song(data)

            return self.respond_success(data = data)
        except Exception as e:
            return self.respond_failure(str(e))

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def create_interpretation(self, song_id, registry, effects):
        try:

            if len(song_id) == 0:
                raise Exception('Empty song ID.')

            if len(registry) == 0:
                raise Exception('Empty registry.')

            if len(effects) == 0:
                effects = []
            else:
                effects = effects.split(',')

            data = {
                'song_id':  int(song_id),
                'registry': str(registry),
                'effects':  list(effects)
            }

            data = self.interpretation.create_interpretation(data)

            return self.respond_success(data = data)
        except Exception as e:
            return self.respond_failure(str(e))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def list_songs(self):
        try:
            songs = self.song.get_all_songs()

            data = {
                'songs': list(songs)
            }

            return self.respond_success(data = data)
        except Exception as e:
            return self.respond_failure(str(e))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def list_song_files(self, id):
        try:
            wave_form_file = self.song.get_song_wave_form_file_by_id(id)
            wave_files = self.interpretation.get_interpretations_wave_files_by_song_id(id)

            data = {
                'wave_form_file': str(wave_form_file),
                'wave_files': list(wave_files)
            }

            return self.respond_success(data = data)
        except Exception as e:
            return self.respond_failure(str(e))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_notes(self, id):
        try:
            notes = self.song.get_song_rtttl_by_id(id)

            data = {
                'notes': str(notes)
            }

            return self.respond_success(data = data)
        except Exception as e:
            return self.respond_failure(str(e))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_wave_file(self, id):
        try:
            interpretation = self.interpretation.get_interpretation_by_id(id)

            data = {
                'wave_file': str(interpretation['wave_file'])
            }

            return self.respond_success(data = data)
        except Exception as e:
            return self.respond_failure(str(e))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_wave_form(self, id):
        try:
            wave_form_file = self.song.get_song_wave_form_file_by_id(id)

            data = {
                'wave_form_file': str(wave_form_file)
            }

            return self.respond_success(data = data)
        except Exception as e:
            return self.respond_failure(str(e))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def submit_vote(self, id, vote):
        try:
            if int(vote) > 0:
                self.interpretation.upvote_interpretation_by_id(id)
            else:
                self.interpretation.downvote_interpretation_by_id(id)
            return self.respond_success()
        except Exception as e:
            return self.respond_failure(str(e))

    @cherrypy.tools.json_out()
    def respond(self, success = True, message = '', data = []):
        output = {
            'success': success,
            'message': message,
            'data': data
        }

        return output

    @cherrypy.tools.json_out()
    def respond_success(self, message = 'Your request was successful.', data = []):
        return self.respond(True, message, data)

    @cherrypy.tools.json_out()
    def respond_failure(self, message = 'Your request was a failure.', data = []):
        return self.respond(False, message, data)
