class Kanjicard:
    def __init__(self, kanji: str = "一"):
        self.kanji = kanji
        self.JLPT = 0
        self.frequency = 0
        self.strokes = 1
        self.readings = {}
        self.meanings = []
        
    def __str__(self):
        return self.kanji + " " + str(self.meanings) + " " + str(self.readings)
        
    def setInfoData(self, jlpt: int, frequency: int, strokes: int):
        self.JLPT = jlpt
        self.frequency = frequency
        self.strokes = strokes

    def addReading(self, reading: str, onyomi: bool):
        self.readings[reading] = onyomi

    def setMeanings(self, meaningsString: str):
        self.meanings = []
        for meaning in meaningsString.split(","):
            self.meanings.append(meaning)
    