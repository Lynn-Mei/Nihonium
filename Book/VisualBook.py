import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QGridLayout, QLabel

from .VisualPages import VisualPages
from .Book import Book

class VisualBook(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.book = None
        self.layout = QtWidgets.QGridLayout(self)
        self.setStyleSheet("background-color: #c99c99;")

    def newBook(self):
        self.book = Book.create("cards.xml")
        self.showBook()
        
    def openBook(self, filePath: str):
        self.book = Book.importBook(filePath)
        self.showBook()
        print(1)
        
    def saveBook(self):
        self.book.save()
        
    def showBook(self):
        self.layout.addWidget(VisualPages(self.book.getPages()), 0, 0)

'''    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))'''