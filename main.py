import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from CardListing import CardListing
from CardManager import CardManager


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.start()
        
    def start(self):
        widget = CardListing()
        self.setCentralWidget(widget)
        self.resize(800, 600)
    
if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
    