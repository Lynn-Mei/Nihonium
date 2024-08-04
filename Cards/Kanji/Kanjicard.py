class Kanjicard:
    def __init__(self, kanji: str = "一", readings: list[str] = ["いち", "いつ", "ひと"], meanings: list[str] = ["one"]):
        self.kanji = kanji
        self.readings = readings
        self.meanings = meanings
        
    def __str__(self):
        return self.kanji + " " + str(self.meanings) + " " + str(self.readings)
        
    def setValues(self, kanji: str, readings: list[str], meanings: list[str]):
        self.kanji = kanji
        self.readings = readings
        self.meanings = meanings
    