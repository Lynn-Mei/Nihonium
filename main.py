import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QFileDialog, QTabWidget
from PySide6.QtGui import QAction
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from Book.Kanji.VisualKanjiList import VisualKanjiList
from Book.Kanji.VisualListsPage import VisualListsPage
from Book.VisualBook import VisualBook
from KnowledgeBase.Kanjisearch import Kanjisearch 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tab = QTabWidget()
        self.start()
        
    def start(self):
        self.resize(800, 600)

        self.tab = QTabWidget()
        self.tab.setTabPosition(QTabWidget.TabPosition.South)
        self.setCentralWidget(self.tab)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('Study Book')
        jp_menu = menubar.addMenu('Japanese')
        
        new_action = QAction('New', self)
        new_action.triggered.connect(self.new_file)

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
    
        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_file)
        
        kanji_action = QAction('Kanji List', self)
        kanji_action.triggered.connect(self.open_kanji_list)
        
        jpdict_action = QAction('Dictionnary', self)
        jpdict_action.triggered.connect(self.open_jp_dictionary)
        
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        jp_menu.addAction(kanji_action)
        jp_menu.addAction(jpdict_action)
        
    def new_file(self):
        book_tab = VisualBook()
        book_tab.newBook()
        self.tab.addTab(book_tab)
        self.tab.setCurrentWidget(book_tab)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)")
        book_tab = VisualBook()
        book_tab.Button_clicked.connect(self.book_button_Clicked)
        book_tab.openBook(file_name)
        self.tab.addTab(book_tab, book_tab.getName())
        self.tab.setCurrentWidget(book_tab)

    def save_file(self):
        book_tab = VisualBook()
        book_tab.saveBook()
        
    def open_kanji_list(self):
        search_tab = Kanjisearch()
        self.tab.addTab(search_tab, "Kanji Dictionary")
        self.tab.setCurrentWidget(search_tab)
        
    def open_jp_dictionary(self):
        print("dict")

    def book_button_Clicked(self, id_btn: int):
        match id_btn:
            case 1:
                self.open_list_view(False)
            case 2:
                self.open_list_view(True)
            case _:
                print("none")

    def open_list_view(self, type: bool):
        list_view: QtWidgets.QWidget = VisualListsPage(type)
        if not type:
            self.tab.addTab(list_view, "Your lists")
        else:
            self.tab.addTab(list_view, "Kanji by JLPT Level")
        self.tab.setCurrentWidget(list_view)


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
    