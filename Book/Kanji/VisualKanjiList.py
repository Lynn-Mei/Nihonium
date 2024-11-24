from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QVBoxLayout, QListWidget, QListWidgetItem

from Book.Kanji.KanjiDAO import KanjiDAO
from Book.Kanji.KanjiList import KanjiList
from Book.Kanji.Kanjicard import Kanjicard

class VisualKanjiList(QtWidgets.QWidget):
    Result_clicked = QtCore.Signal(Kanjicard)

    def __init__(self, cards: KanjiList):
        super().__init__()
        self.cards = cards
        self.rescard_size = 30
        main_layout = QVBoxLayout(self)

        self.results_list = QListWidget(self)
        self.results_list.setViewMode(QListWidget.IconMode)
        self.results_list.setSpacing(self.rescard_size)
        self.results_list.setResizeMode(QListWidget.Adjust)
        self.results_list.setUniformItemSizes(True)
        self.results_list.setIconSize(QtCore.QSize(self.rescard_size, self.rescard_size))

        self.fill_resultlist()

        self.setQSSRules()
        self.results_list.itemClicked.connect(self.detectMemberClick)

        main_layout.addWidget(self.results_list)
        self.setLayout(main_layout)

    def fill_resultlist(self):
        self.results_list.clear()
        for card in self.cards.getCards():
            item = QListWidgetItem(card.kanji)

            font = QtGui.QFont("SansSerif", 24)
            item.setFont(font)

            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setSizeHint(QtCore.QSize(self.rescard_size, self.rescard_size))
            self.results_list.addItem(item)

    def setQSSRules(self):
        self.results_list.setStyleSheet("""
            QListWidget::item {
                background-color: #f0f0f0; 
                padding: 10px;        
                border-radius: 5px; 
            }
            QListWidget::item:hover {
                background-color: #a0c0f0;  
                color: white; 
                font-weight: bold;
                border: 1px solid #6a9fb5;
            }
        """)

    def detectMemberClick(self, item: QListWidgetItem):
        kanji: str = item.text()
        dao: KanjiDAO = KanjiDAO()
        card = dao.getKanjicard(kanji)
        self.Result_clicked.emit(card)