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
        return self.respond_failure('You\'re at the API root.')

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def create_song(self, rtttl):
        try:
            if len(rtttl) == 0:
                raise Exception('Empty RTTTL string.')

            wave_form_file = self.md5(rtttl)

            data = {
                'rtttl': str(rtttl),
                'wave_form_file': 'storage/wave_form_files/' + str(wave_form_file) + '.png'
            }

            song_interpretation = RtttlParser(rtttl).interpret()
            renderer = WaveformImageRenderer(song_interpretation)
            renderer.draw()
            renderer.save(wave_form_file)

            self.song.create_song(data)

            return self.respond_success(data = data)
        except Exception as e:
            return self.respond_failure(str(e))

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def create_interpretation(self, id, registry, effects):
        try:
            data = {
                'song_id':  int(id),
                'registry': str(registry),
                'effects':  str(effects),
                'wave_file': 'storage/wave_files/' + self.md5(str(id)) + '.wav'
            }

            self.interpretation.create_interpretation(data)

            song_rtttl = self.song.get_song_rtttl_by_id(song_id)

            wave_file = self.md5(str(id))
            wav_generator = WavGenerator(registry, song_rtttl, effects)
            wav_generator.create(wave_file)

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
            vote = int(vote)

            self.interpretation.update_interpretation_votes_by_id(id, vote)

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
