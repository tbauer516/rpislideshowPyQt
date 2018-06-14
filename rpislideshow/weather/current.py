from PySide2.QtWidgets import QGridLayout, QLabel, QFrame
from PySide2.QtSvg import QSvgWidget

class Current:

    def __init__(self):
        self.layout = QGridLayout()
        self.wrapper = QFrame()
        self.wrapper.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)

        self.time = QLabel()
        self.icon = QSvgWidget()
        self.temp = QLabel()
        self.precip = QLabel()
        self.wind = QLabel()

        self.layout.addWidget(self.time, 0, 0, 1, 2)
        self.layout.addWidget(self.icon, 1, 0, 3, 1)
        self.layout.addWidget(self.temp, 1, 1, 1, 1)
        self.layout.addWidget(self.wind, 2, 1, 1, 1)
        self.layout.addWidget(self.precip, 3, 1, 1, 1)

    def update(self, values):
        self.icon.load(values.icon)
        self.time.setText(values.time)
        self.temp.setText(values.temp)
        self.wind.setText(values.wind)
        self.precip.setText(values.precip)
