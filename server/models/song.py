from models.base_model import BaseModel

class Song(BaseModel):
    def create_song(self, data):
        self.database.query('INSERT INTO songs(rtttl) VALUES(?)', (data['rtttl'],))

    def get_all_songs(self):
        songs = self.database.fetch('SELECT * FROM songs')
        return songs

    def get_song_by_id(self, id):
        song = self.database.fetch('SELECT * FROM songs WHERE id=?', (id,))
        return song

    def get_song_rtttl_by_id(self, id):
        song = self.database.fetch('SELECT rtttl FROM songs WHERE id=?', (id,))
        return song['rtttl']

    def get_song_wave_form_by_id(self, id):
        song = self.database.fetch('SELECT wave_form FROM songs WHERE id=?', (id,))
        return song['wave_form']

    def update_song_by_id(self, id, data):
        if not data['rtttl'] == None:
            self.database.query('UPDATE songs SET rtttl=? WHERE id=?', (data['rtttl'], id))

    def delete_song_by_id(self, id):
        self.database.query('DELETE FROM songs WHERE id=?', (id,))
