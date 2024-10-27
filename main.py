import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QFileDialog
from PySide6.QtGui import QAction
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from Book.VisualBook import VisualBook


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.start()
        
    def start(self):
        self.widget = VisualBook()
        self.setCentralWidget(self.widget)
        self.resize(800, 600)
        menubar = self.menuBar()
        
        file_menu = menubar.addMenu('Study Book')
        new_action = QAction('New', self)
        new_action.triggered.connect(self.new_file)

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
    
        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_file)
        
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        
    def new_file(self):
        self.widget.newBook()

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)")
        self.widget.openBook(file_name)

    def save_file(self):
        self.widget.saveBook()
    
if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
    