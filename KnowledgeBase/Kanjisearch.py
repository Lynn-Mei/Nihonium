import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QGridLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem

class Kanjisearch(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.rescard_size = 30
        self.layout = QtWidgets.QGridLayout(self)
        
        #Adding search bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search...")
        
        #Adding gridlike result list
        self.results_list = QListWidget(self)
        self.results_list.setViewMode(QListWidget.IconMode)
        self.results_list.setSpacing(self.rescard_size)
        self.results_list.setResizeMode(QListWidget.Adjust)
        self.results_list.setUniformItemSizes(True)        
        self.results_list.setIconSize(QtCore.QSize(self.rescard_size, self.rescard_size))
        
        #Temporary data fill for tests
        self.fill_resultlist()
        
        #Adding widgets to main layout
        self.layout.addWidget(self.search_bar)
        self.layout.addWidget(self.results_list)
        self.setLayout(self.layout)
        
    def fill_resultlist(self):
        kanji_characters = ["日", "本", "語", "学", "生", "漢", "字", "書"]
        for kanji in kanji_characters:
            item = QListWidgetItem(kanji)
            
            font = QtGui.QFont("SansSerif", 24)
            item.setFont(font)
            
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            
            item.setSizeHint(QtCore.QSize(self.rescard_size, self.rescard_size))
            
            # Add item to QListWidget
            self.results_list.addItem(item)