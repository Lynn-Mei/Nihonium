from functools import partial

from PySide6 import QtWidgets
from PySide6.QtWidgets import QGridLayout, QWidget, QHBoxLayout, QLabel, QVBoxLayout

from Settings.ColorSettings import ColorSettings
from Settings.SettingsDAO import SettingsDAO
from Widgets.ColorPicker import ColorPicker


class ThemeView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout: QVBoxLayout = QVBoxLayout(self)
        self.color_settings: ColorSettings = ColorSettings()

        main_color_pickers: QHBoxLayout = QHBoxLayout()
        main_color_pickers.addLayout(self.addColorPicker("Main Color", self.color_settings.getMainColor()))
        main_color_pickers.addLayout(self.addColorPicker("Second Color", self.color_settings.getSecondColor()))
        main_color_pickers.addLayout(self.addColorPicker("Third Color", self.color_settings.getThirdColor()))
        main_color_pickers.addLayout(self.addColorPicker("Hover Color", self.color_settings.getHoverColor()))

        value_color_pickers: QHBoxLayout = QHBoxLayout()
        value_color_pickers.addLayout(self.addColorPicker("Positive Color", self.color_settings.getTypedColor(1)))
        value_color_pickers.addLayout(self.addColorPicker("Negative Color", self.color_settings.getTypedColor(-1)))
        value_color_pickers.addLayout(self.addColorPicker("Neutral Color", self.color_settings.getTypedColor(0)))

        tag_color_pickers: QHBoxLayout = QHBoxLayout()
        tag_color_pickers.addLayout(self.addColorPicker("Tag 1", self.color_settings.getTagColor(0)))
        tag_color_pickers.addLayout(self.addColorPicker("Tag 2", self.color_settings.getTagColor(1)))
        tag_color_pickers.addLayout(self.addColorPicker("Tag 3", self.color_settings.getTagColor(2)))
        tag_color_pickers.addLayout(self.addColorPicker("Tag 4", self.color_settings.getTagColor(3)))
        tag_color_pickers.addLayout(self.addColorPicker("Tag 5", self.color_settings.getTagColor(4)))
        tag_color_pickers.addLayout(self.addColorPicker("Tag 6", self.color_settings.getTagColor(5)))

        self.main_layout.addLayout(main_color_pickers)
        self.main_layout.addLayout(value_color_pickers)
        self.main_layout.addLayout(tag_color_pickers)

        self.setLayout(self.main_layout)

    def addColorPicker(self, label: str, init_color: str):
        picker_layout: QVBoxLayout = QVBoxLayout()
        color_label: QLabel = QLabel(label)
        color_picker: ColorPicker = ColorPicker()
        color_picker.setColor(init_color)
        color_picker.Validate_clicked.connect(partial(self.updateColor, color_picker))

        picker_layout.addWidget(color_label)
        picker_layout.addWidget(color_picker)
        return picker_layout

    def updateColor(self, picker_instance: ColorPicker, color: str):
        #picker_instance.setColor(color)
        print(color)


