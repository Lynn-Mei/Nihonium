from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLabel, QScrollArea

from .CardHeadList import CardHeadList
from .Kanjicard import Kanjicard
from PySide6 import QtCore, QtWidgets, QtGui

class VisualKanjiCard(QtWidgets.QWidget):

    def __init__(self, card: Kanjicard):
        super().__init__()
        self.card = card
        main_layout: QVBoxLayout = QVBoxLayout(self)

        container_widget = QWidget()
        container_layout = QVBoxLayout(container_widget)

        container_layout.addWidget(CardHeadList("Meanings", self.card.meanings, "#3949AB", True))
        header_div: QHBoxLayout = QHBoxLayout()
        kanji_card: QLabel = QLabel(self.card.kanji)
        header_div.addWidget(kanji_card)


        scroll_area = QScrollArea()
        scroll_area.setWidget(container_widget)
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)


        
