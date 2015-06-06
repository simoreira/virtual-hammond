import cherrypy
from models.song import Song
from models.interpretation import Interpretation
from image.waveform_image_renderer import WaveformImageRenderer
from sound.wav_generator import WavGenerator
from sound.rtttl_parser import RtttlParser

class Api(object):
    def __init__(self):
        self.song           = Song()
        self.interpretation = Interpretation()

    def md5(self, string):
        return hashlib.md5(string).hexdigest()

    @cherrypy.expose
    def createSong(self, rtttl):
        data = {
            'rtttl': str(rtttl)
        }

        waveform_filename = self.md5(data['rtttl'])

        renderer = self.waveform_image_renderer(RtttlParser(rtttl).interpret())
        renderer.save(waveform_filename)

        self.song.create_song(data)

    @cherrypy.expose
    def createInterpretation(self, id, registry, effects):
        data = {
            'song_id':  int(id),
            'registry': str(registry),
            'effects':  str(effects)
        }

        self.interpretation.create_interpretation(data)

        song_rtttl = self.song.get_song_rtttl_by_id(song_id)

        wavfile_filename = self.md5(str(id)) + '.wav'
        wav_generator = WavGenerator(song_rtttl)
        wav_generator.create(wavfile_filename)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def listSongs(self):
        songs = self.song.get_all_songs()
        return songs

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def listSongFiles(self, id):
        song_files = [[]]

        interpretations = self.interpretation.get_interpretations_by_song_id(id)

        song_files.append()

        song_files.append([])

        for interpretation in interpretations:
            song_files[1].append(interpretation['id'] + '.wav')


    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getNotes(self, id):
        notes = self.get_song_rtttl_by_id(id)
        return notes

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getWaveFile(self, id):
        interpretation = self.interpretation.get_interpretation_by_id(id)
        return interpretation['wav_file']

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def getWaveForm(self, id):
        song = self.song.get_song_by_id(id)
        return song['id']

    @cherrypy.expose
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
