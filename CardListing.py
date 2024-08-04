import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from CardManager import CardManager
from Kanjicard import Kanjicard
from CardGroup import CardGroup
from VisualCardGroup import VisualCardGroup

class CardListing(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.manager = CardManager()
        self.layout = QtWidgets.QVBoxLayout(self)

    def newProject(self):
        self.manager.createFile("cards.json")
        listing: CardGroup = self.getTestListing()
        visualCardGroup: VisualCardGroup = VisualCardGroup(listing)
        
        self.layout.addWidget(visualCardGroup)
        
    def getTestListing(self):
        listing = CardGroup("Kanji for Numbers")
        listing.add(Kanjicard())
        listing.add(Kanjicard("二", ["に","ふた"], ["two"]))
        listing.add(Kanjicard("三", ["さん","み"], ["three"]))
        return listing
        
    def openProject(self):
        self.manager.importFile()

'''    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))'''