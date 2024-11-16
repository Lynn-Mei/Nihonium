from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout

from Book.Kanji.Kanjicard import Kanjicard
from Book.Kanji.KanjicardVisuals.CardHeadList import CardHeadList


class CardHeadStack(QtWidgets.QWidget):
    def __init__(self, card: Kanjicard):
        super().__init__()
        self.card: Kanjicard = card
        main_layout: QVBoxLayout = QVBoxLayout(self)

        main_layout.addWidget(CardHeadList("Meanings", self.card.meanings, "#D32F2F", True))
        main_layout.addWidget(CardHeadList("Onoyomi", self.card.getYomi(False), "#00695C", True))
        main_layout.addWidget(CardHeadList("Kunyomi", self.card.getYomi(True), "#008CD4", True))

        self.setLayout(main_layout)

