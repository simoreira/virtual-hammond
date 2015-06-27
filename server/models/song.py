from helpers import *
from models.base_model import BaseModel
from sound.rtttl_parser import RtttlParser
from image.waveform_image_renderer import WaveformImageRenderer

class Song(BaseModel):
    def __init__(self, database):
        self.database = database

    def create_song(self, data):
        renderer = WaveformImageRenderer(data['rtttl'])
        renderer.save()

        data['wave_form_file']  = 'storage/wave_form_files/' + str(md5(data['rtttl'])) + '.png'

        try:
            self.database.query('INSERT INTO songs(rtttl, wave_form_file) VALUES(?, ?)', (data['rtttl'], data['wave_form_file']))
            data['id'] = self.database.cursor.lastrowid
        except:
            data['id'] = self.database.fetch('SELECT id FROM songs WHERE rtttl=?', (data['rtttl'],))[0]

        return data

    def get_all_songs(self):
        songs = self.database.fetch('SELECT * FROM songs')
        return songs

    def get_song_by_id(self, id):
        song = self.database.fetch('SELECT * FROM songs WHERE id=?', (id,))
        return song[0]

    def get_song_rtttl_by_id(self, id):
        rtttl = self.database.fetch('SELECT rtttl FROM songs WHERE id=?', (id,))
        return rtttl[0]['rtttl']

    def get_song_wave_form_file_by_id(self, id):
        song = self.database.fetch('SELECT wave_form_file FROM songs WHERE id=?', (id,))
        return song[0]['wave_form_file']
