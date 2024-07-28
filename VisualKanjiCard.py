from Kanjicard import Kanjicard
from PySide6 import QtCore, QtWidgets, QtGui

class VisualKanjiCard(QtWidgets.QWidget):
    def __init__(self, card: Kanjicard):
        super().__init__()
        self.card = card
        self.kanji = QtWidgets.QLabel(card.kanji, alignment=QtCore.Qt.AlignLeft)
        self.kana = QtWidgets.QLabel(card.readings[0], alignment=QtCore.Qt.AlignCenter)
        self.meaning = QtWidgets.QLabel(card.meanings[0] , alignment=QtCore.Qt.AlignRight)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.kanji)
        self.layout.addWidget(self.kana)
        self.layout.addWidget(self.meaning)