from SpotifyTracker import APImanager
from PyQt5 import QtCore
from PyQt5.QtCore import *
import time

class Thread(QtCore.QThread):
    newTrack = pyqtSignal(str)
    newArtist = pyqtSignal(str)
    newCoverArt = pyqtSignal(str)
    newTrackPopularity = pyqtSignal(int)
    manager = APImanager()

    def __init__(self,):
        super(Thread, self).__init__()

    def run(self):
        while True:
            track = self.manager.getCurrentTrack()
            artist = self.manager.getCurrentArtist()
            coverArt = self.manager.getCoverArt()
            trackPopularity = self.manager.getTrackPopularity()
            self.newTrack.emit(track)
            self.newArtist.emit(artist)
            self.newCoverArt.emit(coverArt)
            self.newTrackPopularity.emit(trackPopularity)
            time.sleep(5)