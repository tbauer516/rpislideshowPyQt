from PySide2.QtWidgets import QGridLayout, QLabel, QFrame
from PySide2.QtSvg import QSvgWidget

class Forecast:

    def __init__(self):
        self.layout = QGridLayout()
        self.wrapper = QFrame()
        self.wrapper.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)

        self.icon = QSvgWidget()
        self.day = QLabel()
        self.min_temp = QLabel()
        self.max_temp = QLabel()
        self.precip = QLabel()
        self.wind = QLabel()

        self.layout.addWidget(self.icon, 0, 0, 1, 1)
        self.layout.addWidget(self.day, 1, 0, 1, 1)
        self.layout.addWidget(self.min_temp, 1, 1, 1, 1)
        self.layout.addWidget(self.max_temp, 0, 1, 1, 1)
        self.layout.addWidget(self.wind, 0, 2, 1, 1)
        self.layout.addWidget(self.precip, 1, 2, 1, 1)

    def update(self, values):
        self.icon.load(values.icon)
        self.day.setText(values.day)
        self.min_temp.setText(values.min_temp)
        self.max_temp.setText(values.max_temp)
        self.precip.setText(values.precip)
        self.wind.setText(values.wind)
