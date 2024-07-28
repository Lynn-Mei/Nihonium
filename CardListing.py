import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from CardManager import CardManager

class CardListing(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.manager = CardManager()

    def newProject(self):
        self.manager.createFile("cards.json")
        
    def openProject(self):
        self.manager.importFile()

'''    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))'''