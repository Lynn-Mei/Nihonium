import sqlite3

class AppdataHandler():
    
    def __init__(self):
        self.db_path = "C:\\Users\\shuna\\Desktop\\Nihonium\\Appdata.db"
    
    def searchKanji(self, data):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM Kanji''')
            rows = cursor.fetchall()
        return rows    