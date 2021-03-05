from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from SpotifyTracker import APImanager
from Thread import Thread
import requests


manager = APImanager()
form, base = uic.loadUiType("tracker_gui.ui")

# create pyqt5 window
class Test(base, form):
    def __init__(self):
        super(base, self).__init__()
        self.setupUi(self)
        self.thread = Thread()
        self.thread.newTrack.connect(self.updateCurrentTrack)  
        self.thread.newArtist.connect(self.updateCurrentArtist)
        self.thread.prevTrack.connect(self.updatePreviousTrack)
        self.thread.prevArtist.connect(self.updatePreviousArtist)
        self.thread.newCoverArt.connect(self.updateCoverArt)
        self.thread.newTrackPopularity.connect(self.updateTrackPopularity)
        self.thread.newSessionTime.connect(self.updateSessionTime)
        self.thread.start()

        # button handling
        self.buttonPlayPause.clicked.connect(onPlayPauseClick)
        self.buttonPreviousTrack.clicked.connect(onPreviousTrackClick)
        self.buttonNextTrack.clicked.connect(onNextTrackClick)

    def updateCurrentTrack(self, currentTrack):
        self.labelCurrentTrack.setText(currentTrack)
    def updateCurrentArtist(self, currentArtist):
        self.labelCurrentArtist.setText(currentArtist)
    def updatePreviousTrack(self, previousTrack):
        self.labelPreviousTrack.setText(previousTrack)
    def updatePreviousArtist(self, previousArtist):
        self.labelPreviousArtist.setText(previousArtist)
    def updateCoverArt(self, coverArt):
        coverArtImage = QImage()
        # coverArtImage.loadFromData(requests.get(coverArt).content)
        # self.labelCoverArt.setPixmap(QPixmap(coverArtImage))
        coverArtImage.loadFromData(requests.get(coverArt).content)
        pixmap = QPixmap(coverArtImage)
        pixmap2 = pixmap.scaledToHeight(180)
        self.labelCoverArt.setPixmap(pixmap2)
    def updateTrackPopularity(self, trackPopularity):
        self.trackPopularity.setValue(trackPopularity)
    def updateSessionTime(self, timeString):
        self.labelTime.setText(timeString)
def onPlayPauseClick():
    manager.playPause()

def onPreviousTrackClick():
    manager.previousTrack()

def onNextTrackClick():
    manager.nextTrack()
# run application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())


