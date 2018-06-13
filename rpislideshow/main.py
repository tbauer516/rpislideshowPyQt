import sys
from PySide2 import QtWidgets, QtCore, QtGui
from .weather.current import Current
from .weather.forecast import Forecast

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open("rpislideshow/style.qss", "r").read())
    window = QtWidgets.QWidget()
    window.setGeometry(0, 0, 1280, 720)
    window.setWindowTitle('rpislideshow')

    window_palette = window.palette()
    window_palette.setColor(window.backgroundRole(), QtCore.Qt.black)
    window.setPalette(window_palette)

    # add weather days here
    weather_col_layout = QtWidgets.QVBoxLayout()
    curr = Current()
    weather_col_layout.addLayout(curr.layout)

    day1 = Forecast()
    day2 = Forecast()
    day3 = Forecast()
    day4 = Forecast()
    day5 = Forecast()
    day6 = Forecast()

    weather_col_layout.addLayout(day1.layout)
    weather_col_layout.addLayout(day2.layout)
    weather_col_layout.addLayout(day3.layout)
    weather_col_layout.addLayout(day4.layout)
    weather_col_layout.addLayout(day5.layout)
    weather_col_layout.addLayout(day6.layout)

    # add picture here
    pic_layout = QtWidgets.QHBoxLayout()
    pic_pixmap = QtGui.QPixmap()
    pic_pixmap.load('assets/images/0pZiNmy.jpg')
    pic_wrapper = QtWidgets.QLabel()
    pic_wrapper.setPixmap(pic_pixmap)
    # resize pic_widget to be 16:9 size
    pic_layout.addWidget(pic_wrapper)
    pic_layout.addLayout(weather_col_layout)

    window.setLayout(pic_layout)

    window.showFullScreen()

    sys.exit(app.exec_())

main()
