import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QFileDialog, QTabWidget
from PySide6.QtGui import QAction
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from Book.Kanji.KanjiDAO import KanjiDAO
from Book.Kanji.KanjiList import KanjiList
from Book.Kanji.Kanjicard import Kanjicard
from Book.Kanji.VisualKanjiCard import VisualKanjiCard
from Book.Kanji.VisualKanjiList import VisualKanjiList
from Book.Kanji.VisualListsPage import VisualListsPage
from Book.Printer.PrintedCard import PrintedCards
from Book.VisualBook import VisualBook
from KnowledgeBase.Kanjisearch import Kanjisearch
from Settings.ColorSettings import ColorSettings
from Settings.SettingsDAO import SettingsDAO
from Settings.ThemeView import ThemeView


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tab = QTabWidget()
        self.colorSettings = ColorSettings()
        self.start()
        self.show_main_book()
        
    def start(self):
        self.resize(800, 600)

        self.tab = QTabWidget()
        self.tab.setTabPosition(QTabWidget.TabPosition.South)
        self.tab.setTabsClosable(True)
        self.tab.tabCloseRequested.connect(self.close_tab)
        self.tab.setMovable(True)
        self.setCentralWidget(self.tab)


        menubar = self.menuBar()
        file_menu = menubar.addMenu('Study Book')
        jp_menu = menubar.addMenu('Japanese')
        settings_menu = menubar.addMenu('Settings')

        mainmenu_action = QAction('Main Menu', self)
        mainmenu_action.triggered.connect(self.show_main_book)

        new_action = QAction('New', self)
        new_action.triggered.connect(self.new_file)
    
        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_file)
        
        kanji_action = QAction('Kanji List', self)
        kanji_action.triggered.connect(self.open_kanji_list)
        
        jpdict_action = QAction('Dictionnary', self)
        jpdict_action.triggered.connect(self.open_jp_dictionary)

        print_action = QAction('Print', self)
        print_action.triggered.connect(self.print)

        theme_action = QAction('Theme and Colors', self)
        theme_action.triggered.connect(self.open_theme_settings)

        file_menu.addAction(mainmenu_action)
        file_menu.addAction(new_action)
        file_menu.addAction(save_action)
        jp_menu.addAction(kanji_action)
        jp_menu.addAction(jpdict_action)
        jp_menu.addAction(print_action)
        settings_menu.addAction(theme_action)

        #theme
        menubar.setStyleSheet("background-color: #" + self.colorSettings.getSecondColor() + "; color: white;")
        self.setStyleSheet("background-color: #" + self.colorSettings.getMainColor() + ";")
        self.tab.setStyleSheet("""
                    QTabBar::tab {
                        background-color: '#""" + self.colorSettings.getSecondColor() + """';
                        color: white;
                    }

                    QTabBar::tab:selected {
                        background-color: '#""" + self.colorSettings.getThirdColor() + """';
                        color: black;
                    }

                    QTabBar::tab:hover { /* Hover effect */
                        background: '#""" + self.colorSettings.getThirdColor() + """';
                        color: black;
                    }

                """)

    def show_main_book(self):
        book_tab = VisualBook()
        book_tab.Button_clicked.connect(self.book_button_Clicked)
        book_tab.showBook()
        self.tab.addTab(book_tab, book_tab.getName())
        self.tab.setCurrentWidget(book_tab)

    def new_file(self):
        book_tab = VisualBook()
        book_tab.newBook()
        self.tab.addTab(book_tab)
        self.tab.setCurrentWidget(book_tab)

    def save_file(self):
        book_tab = VisualBook()
        book_tab.saveBook()

    def close_tab(self, index:int):
        self.tab.removeTab(index)

    def open_kanji_list(self):
        search_tab = Kanjisearch()
        search_tab.Result_clicked.connect(self.open_kanjicard)
        self.tab.addTab(search_tab, "Kanji Dictionary")
        self.tab.setCurrentWidget(search_tab)
        
    def open_jp_dictionary(self):
        print("dict")

    def open_theme_settings(self):
        theme_tab = ThemeView()
        self.tab.addTab(theme_tab, "Theme Settings")
        self.tab.setCurrentWidget(theme_tab)

    def book_button_Clicked(self, id_btn: int):
        match id_btn:
            case 1:
                self.open_list_view(False)
            case 2:
                self.open_list_view(True)
            case _:
                print("none")

    def open_list_view(self, type: bool):
        list_view: VisualListsPage = VisualListsPage(type)
        list_view.KanjiListSelected.connect(self.open_inner_list_view)
        if not type:
            self.tab.addTab(list_view, "Your lists")
        else:
            self.tab.addTab(list_view, "Kanji by JLPT Level")
        self.tab.setCurrentWidget(list_view)

    def open_inner_list_view(self, kan_list: KanjiList):
        inner_list_view: VisualKanjiList = VisualKanjiList(kan_list)
        inner_list_view.Result_clicked.connect(self.open_kanjicard)
        self.tab.addTab(inner_list_view, kan_list.title)
        self.tab.setCurrentWidget(inner_list_view)

    def open_kanjicard(self, card: Kanjicard):
        card_view: QtWidgets.QWidget = VisualKanjiCard(card)
        self.tab.addTab(card_view, card.kanji + " - " + card.meanings[0])
        self.tab.setCurrentWidget(card_view)

    def print(self):
        dao: KanjiDAO = KanjiDAO()
        cards:list[Kanjicard] = []

        cards.append(dao.getKanjicard("忘"))
        cards.append(dao.getKanjicard("忘"))
        cards.append(dao.getKanjicard("忘"))
        cards.append(dao.getKanjicard("忘"))
        cards.append(dao.getKanjicard("忘"))
        cards.append(dao.getKanjicard("忘"))
        cards.append(dao.getKanjicard("忘"))
        cards.append(dao.getKanjicard("忘"))

        pcard: PrintedCards = PrintedCards(cards)
        pcard.print_document()

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
    