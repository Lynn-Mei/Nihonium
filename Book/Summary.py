from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QPushButton

from Settings.ColorSettings import ColorSettings


class Summary(QtWidgets.QWidget):

    Button_clicked = QtCore.Signal(int)

    def __init__(self):
        super().__init__()
        self.book = None
        self.layout = QtWidgets.QGridLayout(self)

        self.lists_btn = QPushButton("Custom Kanji Lists")
        self.jlpt_btn = QPushButton("Kanji by JLPT level")
        self.progress_btn = QPushButton("Your progress")
        self.stats_btn = QPushButton("Your statistics")
        self.learn_btn = QPushButton("Learn")
        self.practice_btn = QPushButton("Practice")

        button_size = (100, 75)
        for btn in [self.lists_btn, self.jlpt_btn, self.progress_btn,
                    self.stats_btn, self.learn_btn, self.practice_btn]:
            btn.setMinimumSize(*button_size)
            btn.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.layout.addWidget(self.lists_btn, 0, 0)
        self.layout.addWidget(self.jlpt_btn, 0, 1)
        self.layout.addWidget(self.progress_btn, 0, 2)
        self.layout.addWidget(self.stats_btn, 1, 0)
        self.layout.addWidget(self.learn_btn, 1, 1)
        self.layout.addWidget(self.practice_btn, 1, 2)

        self.lists_btn.clicked.connect(lambda: self.Button_clicked.emit(1))
        self.jlpt_btn.clicked.connect(lambda: self.Button_clicked.emit(2))
        self.progress_btn.clicked.connect(lambda: self.Button_clicked.emit(3))
        self.stats_btn.clicked.connect(lambda: self.Button_clicked.emit(4))
        self.learn_btn.clicked.connect(lambda: self.Button_clicked.emit(5))
        self.practice_btn.clicked.connect(lambda: self.Button_clicked.emit(6))

        colorSettings = ColorSettings()
        self.setStyleSheet("background-color: #" + colorSettings.getThirdColor() + ";")
