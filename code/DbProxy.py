import sqlite3
from code.Decorators import singleton

@singleton
class DbProxy:
    def __init__(self):
        self.conn = sqlite3.connect('game.db')
        self.cursor = self.conn.cursor()
        self.__create_table()

    def __create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS game_scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def add_score(self, name: str, score: int):
        self.cursor.execute('INSERT INTO game_scores (name, score) VALUES (?, ?)', (name, score))
        self.conn.commit()

    def get_top_scores(self, limit: int = 5) -> list:
        self.cursor.execute('SELECT name, score FROM game_scores ORDER BY score DESC LIMIT ?', (limit,))
        return [(row[0], row[1]) for row in self.cursor.fetchall()]

    def __del__(self):
        self.conn.close()
