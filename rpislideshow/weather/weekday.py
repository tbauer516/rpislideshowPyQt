"""class that represents a single day of the week for a weather forecast"""

from PyQt5.QtWidgets import QGridLayout, QLabel
from PyQt5.QtSvg import QSvgWidget

class WeekDay:

    def __init__(self):
        self.layout = QGridLayout()

        self.icon = QSvgWidget()
        self.day = QLabel()
        self.min_temp = QLabel()
        self.max_temp = QLabel()
        self.precip = QLabel()
        self.wind = QLabel()

    def update(self, day, icon, min_temp, max_temp, wind, precip):
        self.icon.load(icon)
        self.day.setText(day)
        self.min_temp.setText(min_temp)
        self.max_temp.setText(max_temp)
        self.precip.setText(precip)
        self.wind.setText(wind)
