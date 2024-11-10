from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QListWidget

from Book.Kanji.KanjiDAO import KanjiDAO
from Book.Kanji.KanjiList import KanjiList
from Book.Kanji.Kanjicard import Kanjicard


class VisualListsPage(QtWidgets.QWidget):
    def __init__(self, type: bool):
        super().__init__()
        self.kanjilists: list[KanjiList] = self.acquire_lists(type)
        self.list_widget: QListWidget = QListWidget()
        main_layout = QVBoxLayout(self)

        for l in self.kanjilists:
            self.list_widget.addItem(l.title)

        main_layout.addWidget(self.list_widget)

    def acquire_lists(self, IsJLPT: bool) -> list[KanjiList]:
        dao: KanjiDAO = KanjiDAO()
        res: list[KanjiList] = []
        print(IsJLPT)
        if not IsJLPT:
            print("da")
            res = dao.getLists()
        else:
            print("o")
            res = [KanjiList("JLPT N1"), KanjiList("JLPT N2"), KanjiList("JLPT N3"), KanjiList("JLPT N4"),
                   KanjiList("JLPT N5")]
        return res
