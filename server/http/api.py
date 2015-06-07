import cherrypy
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
        return self.respond_failure()

    @cherrypy.expose
    def create_song(self, rtttl):
        try:
            wave_form_file = self.md5(rtttl)

            data = {
                'rtttl': str(rtttl),
                'wave_form_file': str(wave_form_file)
            }

            self.song.create_song(data)

            song_interpretation = RtttlParser(rtttl).interpret()
            renderer = self.waveform_image_renderer(song_interpretation)
            renderer.save(waveform_filename)

        except:
            return self.respond_failure()

    @cherrypy.expose
    def create_interpretation(self, id, registry, effects):
        data = {
            'song_id':  int(id),
            'registry': str(registry),
            'effects':  str(effects)
        }

        self.interpretation.create_interpretation(data)

        song_rtttl = self.song.get_song_rtttl_by_id(song_id)

        wave_file = self.md5(str(id)) + '.wav'
        wav_generator    = WavGenerator(song_rtttl)
        wav_generator.create(wave_file)

        return self.respond_success()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def list_songs(self):
        songs = self.song.get_all_songs()

        data = {
            'songs': list(songs)
        }

        return self.respond_success(data = data)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def list_song_files(self, id):
        wave_form_file = self.song.get_song_wave_form_file_by_id(id)
        wave_files = self.interpretation.get_interpretations_wave_files_by_song_id(id)

        data = {
            'wave_form_file': str(wave_form_file),
            'wave_files': list(wave_files)
        }

        return self.respond_success(data = data)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_notes(self, id):
        notes = self.song.get_song_rtttl_by_id(id)

        data = {
            'notes': str(notes)
        }

        return self.respond_success(data = data)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_wave_file(self, id):
        interpretation = self.interpretation.get_interpretation_by_id(id)

        data = {
            'wave_file': str(interpretation['wave_file'])
        }

        return self.respond_success(data = data)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_wave_form(self, id):
        wave_form_file = self.song.get_song_wave_form_file_by_id(id)

        data = {
            'wave_form_file': str(wave_form_file)
        }

        return self.respond_success(data = data)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def vote_interpretation(self, vote, id):
        vote = int(vote)

        wave_form_file = self.interpretation.update_interpretation_votes(id)

        data = {
            'wave_form_file': str(wave_form_file)
        }

        return self.respond_success(data = data)

    def respond(self, message, data):
        output = {
            'message': message,
            'data': data
        }

        return output

    @cherrypy.tools.json_out()
    def respond_success(self, message = 'Your request was successful.', data = []):
        return self.respond(message, data)

    @cherrypy.tools.json_out()
    def respond_failure(self, message = 'Your request was a failure.', data = []):
        return self.respond(message, data)
