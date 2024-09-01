from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QGridLayout, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QScrollArea

class VisualPages(QtWidgets.QWidget):
    def __init__(self, pages):
        super().__init__()
        self.pages = pages
        self.layout = QtWidgets.QGridLayout(self)
        self.left_nav_layout = QtWidgets.QVBoxLayout()
        
        self.book_title = QLabel(self.pages.getBookTitle())
        self.left_nav_layout.addWidget(self.book_title)
        self.layout.addLayout(self.left_nav_layout, 0, 0)
        self.generate_grouplist()

        self.main = QLabel("")
        self.main.setMinimumWidth(700)
        self.layout.addWidget(self.main, 0, 1)
        '''creer nouvelle classe VisualPageGroup pour le code suivant'''
        '''cette classe doit avoir un id donne en init et override mousePressEvent et utiliser une fonction callback'''
        '''ajouter la section gauche qui liste les card groups (onglet voc/kanji)'''
        
    def generate_grouplist(self):
        self.list_widget = QListWidget()
        for i in self.pages.getKanjiGroups():
            item = QListWidgetItem(i)
            self.list_widget.addItem(item)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.list_widget)
        self.left_nav_layout.addWidget(scroll_area)
        
    def page_clicked(self, type, index):
        group = None
        self.layout.removeWidget(self.main)
        if type == "Kanji":
            group = self.pages.openKanjiGroup(index)
        else:
            group = self.pages.openVocGroup(index)
        self.main = VisualKanjiCardGroup(group)
        self.layout.addWidget(self.main)
        '''Retirer tout visualkanji card group precedent'''
        