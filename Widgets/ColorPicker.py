from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QColorDialog, QPushButton, QVBoxLayout, QWidget

class ColorPicker(QWidget):
    Validate_clicked = QtCore.Signal(str)

    def __init__(self, identifier: str):
        super().__init__()
        self.identifier = identifier
        self.layout = QVBoxLayout(self)

        self.button = QPushButton("Pick a Color")
        self.button.clicked.connect(self.open_color_picker)

        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def open_color_picker(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.Validate_clicked.emit(color.getRgb())

    def setColor(self, color:str):
        self.setStyleSheet(f"background-color: #"+ color +";")