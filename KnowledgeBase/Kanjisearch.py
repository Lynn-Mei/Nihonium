import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QGridLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem, QHBoxLayout, QVBoxLayout, QPushButton

from Book.Kanji.KanjiDAO import KanjiDAO
from Book.Kanji.KanjiList import KanjiList
from Book.Kanji.Kanjicard import Kanjicard
from .AppdataHandler import AppdataHandler

class Kanjisearch(QtWidgets.QWidget):
    Result_clicked = QtCore.Signal(Kanjicard)

    def __init__(self):
        super().__init__()
        self.rescard_size = 30
        main_layout = QVBoxLayout(self)
        
        #Adding search bar
        search_layout = QHBoxLayout()
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Type your kanji or its pronounciation...")
        
        self.search_button = QPushButton("Search", self)
        self.search_button.clicked.connect(self.search)
        
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_button)
        
        #Adding gridlike result list
        self.results_list = QListWidget(self)
        self.results_list.setViewMode(QListWidget.IconMode)
        self.results_list.setSpacing(self.rescard_size)
        self.results_list.setResizeMode(QListWidget.Adjust)
        self.results_list.setUniformItemSizes(True)        
        self.results_list.setIconSize(QtCore.QSize(self.rescard_size, self.rescard_size))

        self.setQSSRules()
        self.results_list.itemClicked.connect(self.detectMemberClick)

        #Temporary data fill for tests
        dao:KanjiDAO = KanjiDAO()
        self.fill_resultlist(dao.get_all_kanji(60))
        
        #Adding widgets to main layout
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.results_list)
        self.setLayout(main_layout)
        
    def fill_resultlist(self, kanji_list):
        self.results_list.clear()
        if len(kanji_list) < 1:
            kanji_list = ["航", "本", "語", "学", "生", "漢", "字", "書"]
        for kanji in kanji_list:
            item = QListWidgetItem(kanji)
            
            font = QtGui.QFont("SansSerif", 24)
            item.setFont(font)
            
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setSizeHint(QtCore.QSize(self.rescard_size, self.rescard_size))
            self.results_list.addItem(item)

    def search(self):
        kanji = []
        print(self.search_bar.text())
        handler = AppdataHandler()
        results = handler.searchKanji(self.search_bar.text())
        for res in results:
            kanji.append(res[0])
        print(kanji)
        self.fill_resultlist(kanji)

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
