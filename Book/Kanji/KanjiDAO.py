from .Kanjicard import Kanjicard
from KnowledgeBase.AppdataHandler import AppdataHandler


class KanjiDAO:
    def __init__(self):
        self.Appdata : AppdataHandler = AppdataHandler()

    def __fillCardWithData(self, data_set:list) -> Kanjicard:
        card: Kanjicard = Kanjicard(data_set[0])
        card.setInfoData(data_set[1], data_set[2], data_set[3])
        card.setMeanings(data_set[4])

        reading_data: list = self.Appdata.execute(
            '''SELECT * FROM KanjiReadings WHERE Kanji = "''' + str(data_set[0]) + '''"''')
        for reading in reading_data:
            card.addReading(reading[1],reading[2])
        return card

    def getJLPTKanjicards(self, level:int) -> list[Kanjicard]:
        jlpt_cards : list[Kanjicard] = []
        data : list = self.Appdata.execute('''SELECT * FROM Kanji WHERE JLPT = "'''+ str(level) +'''"''')
        for CardData in data:
            jlpt_cards.append(self.__fillCardWithData(CardData))

        return jlpt_cards
