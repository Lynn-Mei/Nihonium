from Kanjicard import Kanjicard

class CardGroup:
    def __init__(self):
        self.cards: list[Kanjicard] = []
        
    def add(self, card: Kanjicard):
        self.cards.append(card)
        
    def remove(self, card: Kanjicard):
        self.cards.remove(card)
        
    def __str__(self):
        res = ""
        for card in self.cards:
            res += str(card) + "\r\n"
        return res
            
            