import sqlite3

class AppdataHandler():
    
    def __init__(self):
        self.db_path = "C:\\Users\\shuna\\Desktop\\Nihonium\\Appdata.db"
    
    def searchKanji(self, data):
        kanjis = "("
        kanjis += "'" + list(data)[0] + "',"
        for k in list(data):
            kanjis += "'" + k + "',"
        kanjis += "'" + list(data)[0] + "')"
        
        query = '''SELECT * FROM Kanji k LEFT JOIN KanjiReadings r ON r.Kanji = k.Kanji WHERE k.Kanji IN '''+ kanjis +''' OR r.Reading LIKE "%'''+ data +'''%" GROUP BY k.Kanji'''
        return self.execute(query)

    def execute(self, request: str) -> list:
        rows = []
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(request)
            rows = cursor.fetchall()
        return rows