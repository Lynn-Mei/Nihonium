from PySide6 import QtWidgets
from PySide6.QtWidgets import QHBoxLayout

from Book.Kanji.Kanjicard import Kanjicard
from Book.Kanji.KanjicardVisuals.CardHeadStack import CardHeadStack


class CardHead(QtWidgets.QWidget):
    def __init__(self, card: Kanjicard):
        super().__init__()
        self.card: Kanjicard = card
        main_layout: QHBoxLayout = QHBoxLayout(self)

        character: QtWidgets.QLabel = QtWidgets.QLabel(self.card.kanji)
        main_layout.addWidget(character)
        main_layout.addWidget(CardHeadStack(card))

        self.setLayout(main_layout)

