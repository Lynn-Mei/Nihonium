from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QVBoxLayout, QListWidget, QLabel

from Book.Kanji.KanjiDAO import KanjiDAO
from Book.Kanji.KanjiList import KanjiList


class VisualListsPage(QtWidgets.QWidget):
    KanjiListSelected = Signal(KanjiList)

    def __init__(self, type: bool):
        super().__init__()
        self.kanjilists: list[KanjiList] = self.acquire_lists(type)
        main_layout = QVBoxLayout(self)
        for l in self.kanjilists:
            element: VisualPageListElement = VisualPageListElement(l)
            element.Clicked.connect(self.openKanjiList)
            main_layout.addWidget(element)

    def openKanjiList(self, kan_list: KanjiList):
        self.KanjiListSelected.emit(kan_list)

    def acquire_lists(self, IsJLPT: bool) -> list[KanjiList]:
        dao: KanjiDAO = KanjiDAO()
        res: list[KanjiList] = []
        if not IsJLPT:
            res = dao.getLists()
        else:
            res = [KanjiList("JLPT N1"), KanjiList("JLPT N2"), KanjiList("JLPT N3"), KanjiList("JLPT N4"),
                   KanjiList("JLPT N5")]
        return res

class VisualPageListElement(QtWidgets.QWidget):
    Clicked = QtCore.Signal(KanjiList)

    def __init__(self, kan_list:KanjiList):
        super().__init__()
        self.kanjilist:KanjiList = kan_list
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: "#afbab2"')
        self.setMaximumHeight(100)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(QLabel(kan_list.title))

        countstr: str = str(len(kan_list.cards)) + " kanjis"
        self.main_layout.addWidget(QLabel(countstr))

    def enterEvent(self, event):
        self.setStyleSheet('background-color: "#d3e0d7"')

    def leaveEvent(self, event):
        self.setStyleSheet('background-color: "#afbab2"')

    def mousePressEvent(self, event):
        self.Clicked.emit(self.kanjilist)
        super().mousePressEvent(event)