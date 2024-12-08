from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout

from Book.Kanji.Kanjicard import Kanjicard
from Book.Kanji.KanjicardVisuals.CardHeadList import CardHeadList
from Settings.ColorSettings import ColorSettings


class CardHeadStack(QtWidgets.QWidget):
    def __init__(self, card: Kanjicard):
        super().__init__()
        self.card: Kanjicard = card
        main_layout: QVBoxLayout = QVBoxLayout(self)

        colorSettings = ColorSettings()
        main_layout.addWidget(CardHeadList("Meanings", self.card.meanings, colorSettings.tags[0], True))
        main_layout.addWidget(CardHeadList("Onoyomi", self.card.getYomi(False), colorSettings.tags[1], True))
        main_layout.addWidget(CardHeadList("Kunyomi", self.card.getYomi(True), colorSettings.tags[2], True))

        self.setLayout(main_layout)

