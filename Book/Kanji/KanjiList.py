from Book.Kanji.Kanjicard import Kanjicard


class KanjiList:
    def __init__(self, title: str):
        self.title = title
        self.importance = -1
        self.cards: list[Kanjicard] = []

    def setImportance(self, importance):
        self.importance = importance

    def setCards(self, cards: list[Kanjicard]):
        self.cards = cards

    def addKanjicard(self, card: Kanjicard):
        self.cards.append(card)

    def removeKanjicard(self, card: Kanjicard):
        self.cards.remove(card)

    def getTitle(self) -> str:
        return self.title

    def getImportance(self) -> int:
        return self.importance

    def getCards(self) -> list[Kanjicard]:
        return self.cards