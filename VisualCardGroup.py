from CardGroup import CardGroup
from VisualKanjiCard import VisualKanjiCard
from PySide6 import QtCore, QtWidgets, QtGui

class VisualCardGroup(QtWidgets.QWidget):
    def __init__(self, listing: CardGroup):
        super().__init__()
        self.listing = listing
        self.visualListing = []
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.title = QtWidgets.QLabel(self.listing.title)
        self.title.setStyleSheet("font-size: 26px;")
        self.layout.addWidget(self.title)
        self.setFixedSize(200, 75 * len(self.listing.getAll()))
        self.createVisualCards()
        
        
    def createVisualCards(self):
        for card in self.listing.getAll():
            visualCard: VisualKanjiCard = VisualKanjiCard(card)
            self.layout.addWidget(visualCard)
            self.visualListing.append(visualCard)
            