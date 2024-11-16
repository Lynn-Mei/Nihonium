from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLabel, QScrollArea

from Book.Kanji import KanjicardVisuals
from Book.Kanji.Kanjicard import Kanjicard
from Book.Kanji.KanjicardVisuals.CardHead import CardHead
from Book.Kanji.KanjicardVisuals.CardHeadList import CardHeadList
from PySide6 import QtWidgets

from Book.Kanji.KanjicardVisuals.CardStatsWidget import CardStatsWidget


class VisualKanjiCard(QtWidgets.QWidget):

    def __init__(self, card: Kanjicard):
        super().__init__()
        self.card = card
        main_layout: QVBoxLayout = QVBoxLayout(self)

        container_widget = QWidget()
        container_layout = QVBoxLayout(container_widget)

        container_layout.addWidget(CardHead(self.card))
        container_layout.addWidget(CardStatsWidget(self.card))
        header_div: QHBoxLayout = QHBoxLayout()
        kanji_card: QLabel = QLabel(self.card.kanji)
        header_div.addWidget(kanji_card)


        scroll_area = QScrollArea()
        scroll_area.setWidget(container_widget)
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)


        
