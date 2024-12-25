from PySide6 import QtWidgets
from PySide6.QtGui import QPainter
from PySide6.QtCore import QPoint
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QLabel, QGridLayout, QSpacerItem, QSizePolicy

from Book.Kanji.Kanjicard import Kanjicard
from Book.Kanji.KanjicardVisuals.CardHead import CardHead
from Book.Kanji.KanjicardVisuals.CardStatsWidget import CardStatsWidget


class PrintedCards(QtWidgets.QWidget):

    def __init__(self, cards: list[Kanjicard]):
        super().__init__()
        self.cards = cards
        self.main_layout: QGridLayout = QGridLayout(self)
        self.setStyleSheet("background-color: white;")

        self.container_widget = QWidget()
        self.container_layout = QGridLayout(self.container_widget)

        self.container_layout.setContentsMargins(50, 50, 50, 50)
        for i, card in enumerate(self.cards):
            row, col = divmod(i, 2)
            self.container_layout.addWidget(PrintedCard(card), row, col)

        self.main_layout.addWidget(self.container_widget)
        self.setLayout(self.main_layout)

    def print_document(self):
        printer = QPrinter()

        # Show print dialog
        print_dialog = QPrintDialog(printer, self)
        if print_dialog.exec_() == QPrintDialog.Accepted:
            # Use QPainter to print the widget
            painter = QPainter(printer)

            # Render the widget onto the painter
            self.container_widget.render(
                painter, QPoint(0, 0)
            )  # Specify the position explicitly

            # End painting
            painter.end()

class PrintedCard(QtWidgets.QWidget):
    def __init__(self, card: Kanjicard):
        super().__init__()
        self.setStyleSheet("background-color: #F7F7FF;")
        self.setFixedSize(430, 285)
        self.card = card
        self.main_layout: QVBoxLayout = QVBoxLayout(self)

        self.container_widget = QWidget()
        container_layout = QVBoxLayout(self.container_widget)

        container_layout.addWidget(CardHead(self.card))
        container_layout.addWidget(CardStatsWidget(self.card))
        header_div: QHBoxLayout = QHBoxLayout()
        kanji_card: QLabel = QLabel(self.card.kanji)
        header_div.addWidget(kanji_card)

        self.main_layout.addWidget(self.container_widget)
        self.setLayout(self.main_layout)

        


