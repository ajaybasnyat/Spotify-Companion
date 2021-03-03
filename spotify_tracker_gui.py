from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from SpotifyTracker import APImanager
 
manager = APImanager()
track = manager.getPlaying()
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    # win.setGeometry(200,200,300,300)
    win.setWindowTitle("Spotify Session Tracker")

    # label = QtWidgets.QLabel(win)
    # label.setText(track)

    win.setObjectName("MainWindow")
    win.resize(756, 536)
    win.centralwidget = QtWidgets.QWidget(win)
    win.centralwidget.setObjectName("centralwidget")
    win.label = QtWidgets.QLabel(win.centralwidget)
    win.label.setGeometry(QtCore.QRect(270, 10, 101, 16))
    win.label.setObjectName("label")
    win.label.setText("Spotify Tracker")
    win.label_2 = QtWidgets.QLabel(win.centralwidget)
    win.label_2.setGeometry(QtCore.QRect(100, 110, 101, 16))
    win.label_2.setObjectName("label_2")
    win.label_2.setText("Currently Playing:" + track)
    win.label_3 = QtWidgets.QLabel(win.centralwidget)
    win.label_3.setGeometry(QtCore.QRect(100, 160, 101, 16))
    win.label_3.setObjectName("label_3")
    win.label_3.setText("Previous:")
    win.label_4 = QtWidgets.QLabel(win.centralwidget)
    win.label_4.setGeometry(QtCore.QRect(100, 210, 101, 16))
    win.label_4.setObjectName("label_4")
    win.label_4.setText("Next:")
    win.trackHistory = QtWidgets.QListView(win.centralwidget)
    win.trackHistory.setGeometry(QtCore.QRect(340, 110, 341, 341))
    win.trackHistory.setObjectName("trackHistory")
    win.label_5 = QtWidgets.QLabel(win.centralwidget)
    win.label_5.setGeometry(QtCore.QRect(100, 290, 81, 16))
    win.label_5.setObjectName("label_5")
    win.label_5.setText("Session Time:")
    win.graphicsView = QtWidgets.QGraphicsView(win.centralwidget)
    win.graphicsView.setGeometry(QtCore.QRect(80, 320, 161, 121))
    win.graphicsView.setObjectName("graphicsView")
    win.setCentralWidget(win.centralwidget)

    win.show()
    sys.exit(app.exec_())

window()

