import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

from .VisualPages import VisualPages
from .Book import Book

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