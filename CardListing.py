import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from CardManager import CardManager
from Kanjicard import Kanjicard
from VisualKanjiCard import VisualKanjiCard

class CardListing(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)

    def newProject(self):
        self.manager.createFile("cards.json")
        visualCard = VisualKanjiCard(Kanjicard())
        self.layout.addWidget(visualCard)
        
    def openProject(self):
        self.manager.importFile()

'''    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))'''