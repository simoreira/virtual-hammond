from models.base_model import BaseModel

class Song(BaseModel):
    def __init__(self, database):
        self.database = database

    def create_song(self, data):
        self.database.query('INSERT INTO songs(rtttl, wave_form_file) VALUES(?, ?)', (data['rtttl'], data['wave_form_file']))

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
