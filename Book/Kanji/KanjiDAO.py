from .KanjiList import KanjiList
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

    def getLists(self) -> list[KanjiList]:
        lists: list[KanjiList] = []
        data: list = self.Appdata.execute('''SELECT * FROM KanjiList''')
        for listData in data:
            kanjilist = KanjiList(listData[0])
            kanjilist.setImportance(listData[1])
            lists.append(kanjilist)
        return lists

    def fillList(self, kanji_list:KanjiList) -> KanjiList:
        data : list = self.Appdata.execute('''SELECT k.* FROM Kanji k LEFT JOIN ListLinkToKanji l ON k.Kanji = l.Kanji
            WHERE l.ListName = "'''+ kanji_list.getTitle() +'''"''')
        for CardData in data:
            kanji_list.addKanjicard(self.__fillCardWithData(CardData))
        return kanji_list


