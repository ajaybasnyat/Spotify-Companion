from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
 
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("Spotify Tracker")

    label = QtWidgets.QLabel(win)
    label.setText("new label")

    win.show()
    sys.exit(app.exec_())

window()

