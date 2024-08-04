import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

from CardManager import CardManager
from Kanjicard import Kanjicard
from KanjiCardGroup import KanjiCardGroup

from VisualCardGroup import VisualCardGroup

class VisualBook(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.book = None
        self.layout = QtWidgets.QVBoxLayout(self)

    def newBook(self):
        self.book = Book.create("cards.xml")
        self.showBook()
        
    def openBook(self):
        self.book = Book.importBook("cards.xml")
        self.showBook()
        
    def saveBook(self):
        self.book.save()
        
    def showBook(self):
        self.layout.addWidget(VisualPages(self.book.getPages()))

'''    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))'''