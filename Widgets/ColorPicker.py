from PySide6.QtWidgets import QApplication, QColorDialog, QPushButton, QVBoxLayout, QWidget

class ColorPicker(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.button = QPushButton("Pick a Color")
        self.button.clicked.connect(self.open_color_picker)

        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def open_color_picker(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.setStyleSheet(f"background-color: {color.name()};")
            print(f"Selected Color: {color.name()}")

    def set_color(self, color:str):
        self.setStyleSheet(f"background-color: #"+ color +";")