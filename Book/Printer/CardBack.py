from PySide6 import QtWidgets
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QVBoxLayout, QLabel

from Book.Kanji.Kanjicard import Kanjicard


class PrintedCardMeaning(QtWidgets.QWidget):
    def __init__(self, card: Kanjicard):
        super().__init__()
        self.card = card
        self.main_layout: QVBoxLayout = QVBoxLayout(self)

        meanings_str:str = ""
        meanings: list[str]= card.getMeanings()
        for meaning in meanings:
            meanings_str += meaning + ","
        meanings_str = meanings_str[:-1]
        meanings_label: QLabel = QLabel(meanings_str)
        font: QFont = QFont()
        font.setPointSize(26)
        meanings_label.setFont(font)

        self.main_layout.addWidget(meanings_label)
        self.setLayout(self.main_layout)


class PrintedCardVocabulary(QtWidgets.QWidget):
    def __init__(self, card: Kanjicard):
        super().__init__()
        self.card = card
        self.main_layout: QVBoxLayout = QVBoxLayout(self)

        title_label: QLabel = QLabel("Words used")
        font: QFont = QFont()
        font.setPointSize(28)
        title_label.setFont(font)

        self.setLayout(self.main_layout)