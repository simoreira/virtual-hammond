from models.base_model import BaseModel

class Interpretation(BaseModel):
    def create_interpretation(self, data):
        pass

    def get_all_interpretations(self):
        interpretations = self.database.fetch('SELECT * FROM interpretations')
        return interpretations

    def get_interpretation_by_id(self, id):
        interpretation = self.database.fetch('SELECT * FROM interpretations WHERE id=?', (id,))
        return interpretation

    def update_interpretation_by_id(self, id, data):
        pass

    def delete_interpretation_by_id(self, id):
        self.database.query('DELETE FROM interpretations WHERE id=?', (id,))
