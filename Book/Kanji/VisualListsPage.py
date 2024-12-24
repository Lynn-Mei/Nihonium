from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Signal, QSize
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QVBoxLayout, QListWidget, QLabel, QHBoxLayout, QPushButton, QSizePolicy, QWidget

from Book.Kanji.KanjiDAO import KanjiDAO
from Book.Kanji.KanjiList import KanjiList
from Book.Kanji.Kanjicard import Kanjicard
from Settings.ColorSettings import ColorSettings


class VisualListsPage(QtWidgets.QWidget):
    KanjiListSelected = Signal(KanjiList)

    def __init__(self, type: bool):
        super().__init__()
        self.kanjilists: list[KanjiList] = self.acquire_lists(type)
        self.initlists: list[KanjiList] = self.kanjilists
        self.main_layout = QVBoxLayout(self)
        self.refreshList(True)

    def resetMainLayout(self):
        new_layout = QVBoxLayout()
        QWidget().setLayout(self.main_layout)
        self.main_layout = new_layout
        self.setLayout(self.main_layout)

    def refreshList(self, has_subset: bool):
        self.resetMainLayout()

        # Add the header only if not in a subset
        if not has_subset:
            header = self.getHeader()
            self.main_layout.addLayout(header)

        # Add the list elements
        for l in self.kanjilists:
            element: VisualPageListElement = VisualPageListElement(l)
            if has_subset:
                element.Clicked.connect(self.openToSubsets)
            else:
                element.Clicked.connect(self.openKanjiList)
            self.main_layout.addWidget(element)

    def getHeader(self) -> QHBoxLayout:
        header:QHBoxLayout = QHBoxLayout()
        back_button = QPushButton()
        back_button.setIcon(QIcon("assets/arrow.png"))
        back_button.setFixedSize(32, 32)
        back_button.setIconSize(QSize(24, 24))
        back_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
            }
        """)
        back_button.clicked.connect(self.returnFromSubsets)
        header.addWidget(back_button)

        label:QLabel = QLabel("Chirashizushi")
        label_font = QFont()
        label_font.setPointSize(16)  # Set font size to 16 (adjust as needed)
        label.setFont(label_font)
        header.addWidget(label)
        return header

    def openToSubsets(self, clicked_list: KanjiList):
        self.kanjilists: list[KanjiList] = self.acquire_jlptsubset(int(clicked_list.title[-1]))
        self.refreshList(False)

    def returnFromSubsets(self):
        self.kanjilists = self.initlists
        self.refreshList(True)

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
            for i in range(1, 6):
                jlpt_list:KanjiList = KanjiList("JLPT N" + str(i))
                jlpt_list.setCards(dao.getJLPTKanjicards(i))
                res.append(jlpt_list)
        return res

class VisualPageListElement(QtWidgets.QWidget):
    Clicked = QtCore.Signal(KanjiList)

    def __init__(self, kan_list:KanjiList):
        super().__init__()
        self.colorSettings = ColorSettings()
        self.kanjilist:KanjiList = kan_list
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: "#'+ self.colorSettings.getThirdColor() +'"')
        self.setMaximumHeight(100)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(QLabel(kan_list.title))

        countstr: str = str(len(kan_list.cards)) + " kanjis"
        self.main_layout.addWidget(QLabel(countstr))

    def enterEvent(self, event):
        self.setStyleSheet('background-color: "#'+ self.colorSettings.getHoverColor() +'"')

    def leaveEvent(self, event):
        self.setStyleSheet('background-color: "#' + self.colorSettings.getThirdColor() + '"')

    def mousePressEvent(self, event):
        self.Clicked.emit(self.kanjilist)
        super().mousePressEvent(event)