import os

from PySide6 import QtWidgets
from PySide6.QtGui import QPainter, QFont, QPixmap, QPageSize
from PySide6.QtCore import QPoint
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QLabel, QGridLayout, QSpacerItem, QSizePolicy

from Book.Kanji.Kanjicard import Kanjicard
from Book.Kanji.KanjicardVisuals.CardHead import CardHead
from Book.Kanji.KanjicardVisuals.CardStatsWidget import CardStatsWidget
from Book.Printer.CardFront import PrintedCardHead, PrintedCardSounds


class PrintedCards(QtWidgets.QWidget):

    def __init__(self, cards: list[Kanjicard]):
        super().__init__()
        self.cards = cards
        self.main_layout: QGridLayout = QGridLayout(self)

        self.container_widget = QWidget()
        self.container_layout = QGridLayout(self.container_widget)


        for i, card in enumerate(self.cards):
            row, col = divmod(i, 2)
            self.container_layout.addWidget(PrintedCard(card), row, col)

        self.main_layout.addWidget(self.container_widget)
        self.setLayout(self.main_layout)

    def print_document(self):
        printer = QPrinter()
        print_dialog = QPrintDialog(printer, self)
        if print_dialog.exec_() == QPrintDialog.Accepted:
            painter = QPainter(printer)
            self.container_widget.render(
                painter, QPoint(0, 0)
            )
            painter.end()

class PrintedCard(QtWidgets.QWidget):
    def __init__(self, card: Kanjicard):
        super().__init__()
        self.setFixedSize(453, 322)
        self.card = card

        path:str = os.path.join(os.path.dirname(__file__), "NihoniumCard1-1.png")
        self.background_image = QPixmap(path)

        self.main_layout: QVBoxLayout = QVBoxLayout(self)
        self.container_widget = QWidget()
        self.container_widget.setStyleSheet("background-color: transparent;")
        container_layout = QVBoxLayout(self.container_widget)
        self.setStyleSheet("background-color: transparent;")
        """container_layout.addWidget(PrintedCardHead(self.card))
        container_layout.addWidget(PrintedCardSounds(self.card))"""

        graphicsview:QtWidgets.QGraphicsView = QtWidgets.QGraphicsView()
        graphicsview.setStyleSheet("background: transparent; border: none;")
        scene:QtWidgets.QGraphicsScene = QtWidgets.QGraphicsScene(graphicsview)
        graphicsview.setScene(scene)

        proxy:QtWidgets.QGraphicsProxyWidget = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(self.container_widget)
        proxy.setTransformOriginPoint(proxy.boundingRect().center())
        proxy.setRotation(90)
        scene.addItem(proxy)

        self.main_layout.addWidget(graphicsview)
        self.setLayout(self.main_layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.background_image.scaled(self.size()))
        super().paintEvent(event)