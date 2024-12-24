from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout

from Book.Kanji.KanjiDAO import KanjiDAO
from Book.Kanji.Kanjicard import Kanjicard

class CardStatsWidget(QtWidgets.QWidget):
    def __init__(self, card: Kanjicard):
        super().__init__()
        self.card = card
        main_layout: QVBoxLayout = QVBoxLayout(self)

        dao: KanjiDAO = KanjiDAO()
        first_seen:str = dao.getFirstSeen(self.card.kanji)
        last_seen:str =dao.getFirstSeen(self.card.kanji)

        main_layout.addWidget(CardStatsWidgetElement("Identifier", str(card.getIdentifer())))
        main_layout.addWidget(CardStatsWidgetElement("JLPT", str(card.getJLPT())))
        main_layout.addWidget(CardStatsWidgetElement("Strokes", str(card.getStrokes())))
        main_layout.addWidget(CardStatsWidgetElement("Frequency", str(card.getFrequency())))
        main_layout.addWidget(CardStatsWidgetElement("First Seen", str(first_seen[0])))
        main_layout.addWidget(CardStatsWidgetElement("Last Seen", str(last_seen[0])))
        main_layout.addWidget(CardStatsWidgetElement("Mastery", "0"))


        self.setLayout(main_layout)


class CardStatsWidgetElement(QtWidgets.QWidget):
    def __init__(self, label:str, value:str):
        super().__init__()
        main_layout: QHBoxLayout = QHBoxLayout(self)

        main_layout.addWidget(QtWidgets.QLabel(label))
        main_layout.addWidget(QtWidgets.QLabel(value))

        self.setLayout(main_layout)