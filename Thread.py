from SpotifyTracker import APImanager
from PyQt5 import QtCore
from PyQt5.QtCore import *
import time

class Thread(QtCore.QThread):
    newTrack = pyqtSignal(str)
    newArtist = pyqtSignal(str)
    prevTrack = pyqtSignal(str)
    prevArtist = pyqtSignal(str)
    newCoverArt = pyqtSignal(str)
    newTrackPopularity = pyqtSignal(int)
    newSessionTime = pyqtSignal(str)
    manager = APImanager()
    

    def __init__(self,):
        super(Thread, self).__init__()

    def run(self):
        previousTrack = ''
        recentTrack = ''
        previousArtist = ''
        recentArtist = ''
  
        timer = [0, 0, 0]
        pattern = '{0:02d}:{1:02d}:{2:02d}'
        timeString = '00:00:00'
        while True:
            currentTrack = self.manager.getCurrentTrack()
            currentArtist = self.manager.getCurrentArtist()
            coverArt = self.manager.getCoverArt()
            trackPopularity = self.manager.getTrackPopularity()
            isPlaying = self.manager.isPlaying()
            if currentTrack != recentTrack:
                previousTrack = recentTrack
                previousArtist = recentArtist
                recentTrack = currentTrack
                recentArtist = currentArtist

            if isPlaying:
                timer[2] += 1
                if (timer[2] >= 60):
                    timer[2] = 0
                    timer[1] += 1
                if (timer[1] >= 60):
                    timer[0] += 1
                    timer[1] = 0
                timeString = pattern.format(timer[0], timer[1], timer[2])

            self.newTrack.emit(currentTrack)
            self.newArtist.emit(currentArtist)
            self.prevTrack.emit(previousTrack)
            self.prevArtist.emit(previousArtist)
            self.newCoverArt.emit(coverArt)
            self.newTrackPopularity.emit(trackPopularity)
            self.newSessionTime.emit(timeString)
            time.sleep(1)