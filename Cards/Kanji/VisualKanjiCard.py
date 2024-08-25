from .Kanjicard import Kanjicard
from PySide6 import QtCore, QtWidgets, QtGui

class VisualKanjiCard(QtWidgets.QWidget):
    def __init__(self, card: Kanjicard):
        super().__init__()
        self.card = card
        
        self.setFixedSize(200, 75)
        self.kanji = QtWidgets.QLabel(card.kanji)
        self.kana = QtWidgets.QLabel(card.readings[0])
        self.meaning = QtWidgets.QLabel(card.meanings[0])
        
        self.kanji.setStyleSheet("font-size: 21px;")
        self.kana.setStyleSheet("font-size: 21px;")
        self.meaning.setStyleSheet("font-size: 21px;")
        
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.kanji)
        self.layout.addWidget(self.kana)
        self.layout.addWidget(self.meaning)
        
        self.setStyleSheet("background-color: lightblue;")
        
