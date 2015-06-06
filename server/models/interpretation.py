from models.base_model import BaseModel

class Interpretation(BaseModel):
    def create_interpretation(self, data):
        if not data['song_id'] == None and not data['registry'] == None and not data['effects'] == None:
            self.database.query('INSERT INTO interpretations(song_id, registry, effects) VALUES(?, ?, ?)', (data['song_id'], data['registry'], data['effects']))

    def get_all_interpretations(self):
        interpretations = self.database.fetch('SELECT * FROM interpretations')
        return interpretations

    def get_interpretation_by_id(self, id):
        interpretation = self.database.fetch('SELECT * FROM interpretations WHERE id=?', (id,))
        return interpretation

    def get_interpretations_by_song_id(self, song_id):
        interpretations = self.database.fetch('SELECT * FROM interpretations WHERE song_id=?', (song_id,))
        return interpretations

    def update_interpretation_by_id(self, id, data):
        if not data['song_id'] == None:
            self.database.query('UPDATE interpretations SET song_id=? WHERE id=?', (data['song_id'], id))
        if not data['registry'] == None:
            self.database.query('UPDATE interpretations SET registry=? WHERE id=?', (data['registry'], id))
        if not data['effects'] == None:
            self.database.query('UPDATE interpretations SET effects=? WHERE id=?', (data['effects'], id))

    def delete_interpretation_by_id(self, id):
        self.database.query('DELETE FROM interpretations WHERE id=?', (id,))
