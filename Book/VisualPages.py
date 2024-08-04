from PySide6 import QtCore, QtWidgets, QtGui

class VisualPages(QtWidgets.QWidget):
    def __init__(self, pages):
        super().__init__()
        self.pages = pages
        self.layout = QtWidgets.QVBoxLayout(self)
        '''creer nouvelle classe VisualPageGroup pour le code suivant'''
        '''cette classe doit avoir un id donne en init et override mousePressEvent et utiliser une fonction callback'''
        '''ajouter la section gauche qui liste les card groups (onglet voc/kanji)'''
        
    def page_clicked(self, type, index):
        group = None
        if type == "Kanji":
            group = self.pages.openKanjiGroup(index)
        else:
            group = self.pages.openVocGroup(index)
        self.layout.addWidget(VisualKanjiCardGroup(group))
        '''Retirer tout visualkanji card group precedent'''
        