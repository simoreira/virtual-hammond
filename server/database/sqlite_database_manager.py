import sqlite3

class SqliteDatabaseManager:
    def __init__(self, database_name):
        self.connection             = sqlite3.connect(database_name, check_same_thread = False)
        self.connection.row_factory = sqlite3.Row
        self.cursor                 = self.connection.cursor()

    def query(self, query, params = ()):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except Exception as exception:
            self.connection.rollback()
            raise exception

    def fetch(self, query, params = ()):
        self.query(query, params)
        records = self.cursor.fetchall()
        rows = [dict(record) for record in records]
        return rows

    def __del__(self):
        self.connection.close()
