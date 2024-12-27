from PySide6 import QtWidgets
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QVBoxLayout, QLabel

from Book.Kanji.Kanjicard import Kanjicard


class PrintedCardHead(QtWidgets.QWidget):
    def __init__(self, card: Kanjicard):
        super().__init__()
        self.setFixedSize(200, 285)
        self.card = card
        self.main_layout: QVBoxLayout = QVBoxLayout(self)

        kan: QLabel = QLabel(self.card.getCharacter())
        font: QFont = QFont()
        font.setPointSize(45)
        kan.setFont(font)

        self.main_layout.addWidget(kan)
        self.setLayout(self.main_layout)

class PrintedCardSounds(QtWidgets.QWidget):
    def __init__(self, card: Kanjicard):
        super().__init__()
        self.main_layout: QVBoxLayout = QVBoxLayout(self)
        self.card: Kanjicard = card

        self.main_layout.addWidget(PrintedCardSoundsPart("Kunyomi", self.card.getYomi(True)))
        self.main_layout.addWidget(PrintedCardSoundsPart("Onyomi", self.card.getYomi(False)))

        self.setLayout(self.main_layout)

class PrintedCardSoundsPart(QtWidgets.QWidget):
    def __init__(self, label:str, readings: list[str]):
        super().__init__()
        self.main_layout: QVBoxLayout = QVBoxLayout(self)
        self.readings: list[str] = readings

        label: QLabel = QLabel(label)
        self.main_layout.addWidget(label)
        for reading in readings:
            tag: QLabel = QLabel(reading)
            self.main_layout.addWidget(tag)
        self.setLayout(self.main_layout)