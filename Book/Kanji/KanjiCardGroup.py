from Book.Kanji.Kanjicard import Kanjicard


class KanjiCardGroup:
    def __init__(self, title: str):
        self.title = title
        self.cards: list[Kanjicard] = []
        
    def add(self, card: Kanjicard):
        self.cards.append(card)
        
    def remove(self, card: Kanjicard):
        self.cards.remove(card)
        
    def getAll(self):
        return self.cards
        
    def getTitle(self):
        return self.title
        
    def setTitle(self, title):
        self.title = title
        
    def __str__(self):
        res = ""
        for card in self.cards:
            res += str(card) + "\r\n"
        return res