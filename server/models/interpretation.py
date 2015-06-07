from models.base_model import BaseModel

class Interpretation(BaseModel):
    def __init__(self, database):
        self.database = database

    def create_interpretation(self, data):
        if not data['song_id'] == None and not data['registry'] == None and not data['effects'] == None and not data['wave_file'] == None and not data['votes'] == None:
            self.database.query('INSERT INTO interpretations(song_id, registry, effects, wave_file, votes) VALUES(?, ?, ?, ?, ?)', (data['song_id'], data['registry'], data['effects'], data['wave_file'], data['votes']))

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
        wave_files = self.database.fetch('SELECT wave_file FROM interpretations WHERE song_id=?', (song_id,))
        return wave_files
