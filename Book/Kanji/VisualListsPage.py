from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QListWidget

from Book.Kanji.KanjiDAO import KanjiDAO
from Book.Kanji.KanjiList import KanjiList

class VisualListsPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.kanjilists: list[KanjiList] = self.acquire_lists()
        self.list_widget: QListWidget = QListWidget()
        main_layout = QVBoxLayout(self)

        for l in self.kanjilists:
            self.list_widget.addItem(l.title)

        main_layout.addWidget(self.list_widget)

    def acquire_lists(self) -> list[KanjiList]:
        dao: KanjiDAO = KanjiDAO()
        return dao.getLists()

