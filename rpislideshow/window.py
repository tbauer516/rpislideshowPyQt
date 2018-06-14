import sys
from PySide2 import QtWidgets, QtCore, QtGui
from .weather.current import Current
from .weather.forecast import Forecast

class Window:

    app = None
    window = None
    screen_size = None
    debug = True

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setStyleSheet(open("rpislideshow/style.qss", "r").read())
        self.screen_size = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle('rpislideshow')
        self.window.setObjectName('window')

        # add weather days here
        weather_col_wrapper = QtWidgets.QFrame()
        weather_col_layout = QtWidgets.QVBoxLayout()
        weather_col_layout.setSpacing(0)
        weather_col_layout.setContentsMargins(0,0,0,0)
        weather_col_wrapper.setLayout(weather_col_layout)
        # weather_col_wrapper.setFixedWidth(200)

        curr = Current()
        weather_col_layout.addWidget(curr.wrapper)

        day1 = Forecast()
        day2 = Forecast()
        day3 = Forecast()
        day4 = Forecast()
        day5 = Forecast()
        day6 = Forecast()

        weather_col_layout.addWidget(day1.wrapper)
        weather_col_layout.addWidget(day2.wrapper)
        weather_col_layout.addWidget(day3.wrapper)
        weather_col_layout.addWidget(day4.wrapper)
        weather_col_layout.addWidget(day5.wrapper)
        weather_col_layout.addWidget(day6.wrapper)

        # add picture here
        win_layout = QtWidgets.QHBoxLayout()
        win_layout.setSpacing(0)
        pic_pixmap = QtGui.QPixmap()
        pic_pixmap.load('assets/images/0pZiNmy.jpg')
        pic_pixmap_scaled = pic_pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
        pic_wrapper = QtWidgets.QLabel()
        pic_wrapper.setPixmap(pic_pixmap_scaled)
        pic_wrapper.setAlignment(QtCore.Qt.AlignCenter)
        # resize pic_widget to be 16:9 size

        win_layout.addWidget(pic_wrapper)
        win_layout.addWidget(weather_col_wrapper)

        self.window.setLayout(win_layout)

    def start(self):
        if (self.debug):
            self.window.setGeometry(0, 0, 1280, 720)
            self.window.show()
        else:
            self.window.setGeometry(0, 0, self.screen_size.width(), self.screen_size.height())
            self.window.showFullScreen()

        sys.exit(self.app.exec_())
