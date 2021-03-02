from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
from SpotifyTracker import APImanager
 
manager = APImanager()
track = manager.getPlaying()
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("Spotify Tracker")

    label = QtWidgets.QLabel(win)
    label.setText(track)

    win.show()
    sys.exit(app.exec_())

window()

