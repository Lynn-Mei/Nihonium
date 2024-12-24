from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QVBoxLayout, QListWidget, QLabel

from Book.Kanji.KanjiDAO import KanjiDAO
from Book.Kanji.KanjiList import KanjiList
from Book.Kanji.Kanjicard import Kanjicard


class VisualListsPage(QtWidgets.QWidget):
    KanjiListSelected = Signal(KanjiList)

    def __init__(self, type: bool):
        super().__init__()
        self.kanjilists: list[KanjiList] = self.acquire_lists(type)
        self.initlists: list[KanjiList] = self.kanjilists
        self.main_layout = QVBoxLayout(self)
        self.refreshList(True)

    def refreshList(self, has_subset:bool):
        while self.main_layout.count():
            child = self.main_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for l in self.kanjilists:
            element: VisualPageListElement = VisualPageListElement(l)
            if has_subset:
                element.Clicked.connect(self.openToSubsets)
            else:
                element.Clicked.connect(self.openKanjiList)
            self.main_layout.addWidget(element)

    def openToSubsets(self, clicked_list: KanjiList):
        self.kanjilists: list[KanjiList] = self.acquire_jlptsubset(int(clicked_list.title[-1]))
        self.refreshList(False)

    def openKanjiList(self, kan_list: KanjiList):
        self.KanjiListSelected.emit(kan_list)

    def acquire_jlptsubset(self, jlpt_number: int) -> list[KanjiList]:
        dao: KanjiDAO = KanjiDAO()
        subsets: list[KanjiList] = []
        subsets_data: dict[str, list[Kanjicard]] = dao.getJLPTSubset(jlpt_number)
        for k in subsets_data.keys():
            iter_subset: list[Kanjicard] = subsets_data[k]
            kanlist: KanjiList = KanjiList(iter_subset[0].kanji)
            kanlist.setCards(iter_subset)
            kanlist.setImportance(5)
            subsets.append(kanlist)

        return subsets


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