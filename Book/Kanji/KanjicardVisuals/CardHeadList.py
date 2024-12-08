from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QHBoxLayout, QLabel


class CardHeadList(QtWidgets.QWidget):

    def __init__(self, label: str, dataset:list[str], color: str, text: bool):
        super().__init__()
        main_layout: QHBoxLayout = QHBoxLayout(self)

        label_size: QSize = QSize(80, 60)
        main_label = QLabel(label)
        main_label.setMaximumSize(label_size)
        main_layout.addWidget(QLabel(label))

        text_color = "black"
        if text:
            text_color = "white"
        for data in dataset:
            tag: QLabel = QLabel(data)
            tag.setStyleSheet("QLabel { background-color: '#" + color +
                              "'; color: '"+ text_color +"'; border-radius: 25px; padding: 5px; }")
            tag.setAlignment(QtCore.Qt.AlignCenter)
            tag.setMaximumSize(label_size)
            main_layout.addWidget(tag)

        

        self.setLayout(main_layout)