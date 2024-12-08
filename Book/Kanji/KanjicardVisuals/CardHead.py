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

        font = character.font()  # Get the default font
        font.setPointSize(64)    # Set the font size to 32 (adjust as needed)
        character.setFont(font)  # Apply the font to the QLabel

        # Set the size policy to expand vertically and horizontally
        character.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                 QtWidgets.QSizePolicy.Policy.Expanding)

        main_layout.addWidget(character, 1)
        main_layout.addWidget(CardHeadStack(card), 2)

        self.setLayout(main_layout)

