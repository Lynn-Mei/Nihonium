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
            temp_res:list[KanjiList]= dao.getLists()
            for kan_list in temp_res:
                res.append(dao.fillList(kan_list))
        else:
            res: list[KanjiList] = []
            for i in range(1, 5):
                jlpt_list:KanjiList = KanjiList("JLPT N" + str(i))
                jlpt_list.setCards(dao.getJLPTKanjicards(i))
                res.append(jlpt_list)
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