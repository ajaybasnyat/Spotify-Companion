from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from SpotifyTracker import APImanager
from Thread import Thread


manager = APImanager()
form, base = uic.loadUiType("test.ui")

# create pyqt5 window
class Test(base, form):
    def __init__(self):
        super(base, self).__init__()
        self.setupUi(self)
        self.thread = Thread()
        self.thread.newTrack.connect(self.updateLabel)  
        self.thread.start()
    def updateLabel(self, track):
        self.label.setText(track)

# run application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())


