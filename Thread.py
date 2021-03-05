from SpotifyTracker import APImanager
from PyQt5 import QtCore
from PyQt5.QtCore import *
import time

class Thread(QtCore.QThread):
    newTrack = pyqtSignal(str)
    manager = APImanager()

    def __init__(self,):
        super(Thread, self).__init__()

    def run(self):
        while True:
            track = self.manager.getCurrentTrack()
            self.newTrack.emit(track)
            time.sleep(5)