from helpers import *
from models.base_model import BaseModel
from models.song import Song
from sound.wav_generator import WavGenerator

class Interpretation(BaseModel):
    def __init__(self, database):
        self.song     = Song(database)
        self.database = database

    def create_interpretation(self, data):
        data['wave_file'] = 'storage/wave_files/' + md5(str(data['song_id']) + data['registry'] + list_to_csv(data['effects'])) + '.wav'

        rtttl = self.song.get_song_rtttl_by_id(data['song_id'])
        wav_generator = WavGenerator(data['song_id'], data['registry'], rtttl, data['effects'])
        wav_generator.save()

        data['effects'] = list_to_csv(data['effects'])

        self.database.query('INSERT INTO interpretations(song_id, registry, effects, wave_file, votes) VALUES(?, ?, ?, ?, ?)', (data['song_id'], data['registry'], data['effects'], data['wave_file'], 0))

        data['id'] = self.database.cursor.lastrowid

        return data

    def get_all_interpretations(self):
        interpretations = self.database.fetch('SELECT * FROM interpretations')
        return interpretations

    def get_interpretation_by_id(self, id):
        interpretation = self.database.fetch('SELECT * FROM interpretations WHERE id=?', (id,))
        return interpretation[0]

    def get_interpretation_votes_by_id(self, id):
        interpretation = self.database.fetch('SELECT votes FROM interpretations WHERE id=?', (id,))
        return interpretation[0]['votes']

    def get_interpretations_by_song_id(self, song_id):
        interpretations = self.database.fetch('SELECT * FROM interpretations WHERE song_id=?', (song_id,))
        return interpretations

    def get_interpretations_wave_files_by_song_id(self, song_id):
        wave_files = self.database.fetch('SELECT * FROM interpretations WHERE song_id=?', (song_id,))
        return wave_files

    def upvote_interpretation_by_id(self, id):
        self.database.query('UPDATE interpretations SET votes = votes + 1 WHERE id=?', (id,))

    def downvote_interpretation_by_id(self, id):
        self.database.query('UPDATE interpretations SET votes = votes - 1 WHERE id=?', (id,))

