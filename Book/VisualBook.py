import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QGridLayout, QLabel, QBoxLayout
from .Summary import Summary
from .Book import Book

class VisualBook(QtWidgets.QWidget):

    Button_clicked = QtCore.Signal(int)

    def __init__(self):
        super().__init__()
        self.book = None
        self.layout = QtWidgets.QBoxLayout(QBoxLayout.Direction.TopToBottom)
        self.setLayout(self.layout)
        self.summary: Summary = Summary()

    def newBook(self):
        self.book = Book.create("cards.xml")
        self.showBook()
        
    def saveBook(self):
        self.book.save()
        
    def showBook(self):
        self.layout.addWidget(self.summary)
        self.summary.Button_clicked.connect(self.handleButtonClicked)

    def handleButtonClicked(self, id_btn: int):
        self.Button_clicked.emit(id_btn)

    def getName(self)->str:
        return "Study Book" #self.book.bookTitle

'''    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))'''