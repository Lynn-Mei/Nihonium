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

        value_color_pickers: QHBoxLayout = QHBoxLayout()
        value_color_pickers.addLayout(self.addColorPicker("Positive Color", self.color_settings.getTypedColor(1)))
        value_color_pickers.addLayout(self.addColorPicker("Negative Color", self.color_settings.getTypedColor(-1)))
        value_color_pickers.addLayout(self.addColorPicker("Neutral Color", self.color_settings.getTypedColor(0)))

        self.main_layout.addLayout(value_color_pickers)

        self.setLayout(self.main_layout)

    def addColorPicker(self, label: str, init_color: str):
        picker_layout: QVBoxLayout = QVBoxLayout()
        color_label: QLabel = QLabel(label)
        color_picker: ColorPicker = ColorPicker()
        color_picker.set_color(init_color)

        picker_layout.addWidget(color_label)
        picker_layout.addWidget(color_picker)
        return picker_layout