from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QGridLayout, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QScrollArea
from Cards.Kanji.VisualKanjiCardGroup import VisualKanjiCardGroup

class VisualPages(QtWidgets.QWidget):
    def __init__(self, pages):
        super().__init__()
        self.pages = pages
        self.layout = QtWidgets.QGridLayout(self)
        self.left_nav_layout = QtWidgets.QVBoxLayout()
        
        self.book_title = QLabel(self.pages.getBookTitle())
        self.book_title.setMaximumWidth(400)
        self.left_nav_layout.addWidget(self.book_title)
        self.layout.addLayout(self.left_nav_layout, 0, 0)
        self.generate_grouplist()

        self.main = QLabel("")
        '''self.main.setMinimumWidth(700)'''
        self.layout.addWidget(self.main, 0, 1)
        '''creer nouvelle classe VisualPageGroup pour le code suivant'''
        '''cette classe doit avoir un id donne en init et override mousePressEvent et utiliser une fonction callback'''
        '''ajouter la section gauche qui liste les card groups (onglet voc/kanji)'''
        
    def generate_grouplist(self):
        self.list_widget = QListWidget()
        count = 0
        groups_paths = self.pages.getKanjiGroupsPaths()
        for i in self.pages.getKanjiGroups():
            item = QListWidgetItem(i)
            item.setData(1, count)
            self.list_widget.addItem(item)
            count+=1
            
        self.list_widget.itemClicked.connect(self.page_clicked_kan)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.list_widget)
        scroll_area.setMaximumWidth(400)
        self.left_nav_layout.addWidget(scroll_area)
        
    def page_clicked_kan(self, item):
        return self.page_clicked(item, "Kanji")
        
    def page_clicked_voc(self, item):
        return self.page_clicked(item, "Voc")
        
    def page_clicked(self, item, type):
        index = item.data(1)
        group = None
        self.layout.removeWidget(self.main)
        if type == "Kanji":
            group = self.pages.openKanjiGroup(index)
        else:
            group = self.pages.openVocGroup(index)
        self.main = VisualKanjiCardGroup(group)
        self.layout.addWidget(self.main, 0, 1)
        '''Retirer tout visualkanji card group precedent'''
        