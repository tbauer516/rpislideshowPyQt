import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

def main():
	app = QtWidgets.QApplication(sys.argv)
	window = QtWidgets.QWidget()
	window.setGeometry(0, 0, 1280, 720)
	window.setWindowTitle('rpislideshow')

	windowPalette = window.palette()
	windowPalette.setColor(window.backgroundRole(), QtCore.Qt.black)
	window.setPalette(windowPalette)

	weatherColLayout = QtWidgets.QVBoxLayout()
	# add weather days here

	picLayout = QtWidgets.QHBoxLayout()
	# add picture here
	picLayout.addLayout(weatherColLayout)

	window.setLayout(picLayout)

	window.showFullScreen()

	sys.exit(app.exec_())

main()