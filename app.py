from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from APIHandler import APIHandler
from Thread import Thread
import requests
import sys

# create handler for api interactions
handler = APIHandler()
# load in UI form
form, base = uic.loadUiType("tracker_gui.ui")
# list to track listening history
trackHistory = []

# create pyqt5 window
class Window(base, form):
    def __init__(self):
        super(base, self).__init__()
        # default setup
        self.setupUi(self)

        # create thread for updating the GUI
        self.thread = Thread()
        # connect thread of incoming data to updateData method
        self.thread.newData.connect(self.updateData)
        # start thread
        self.thread.start()

        # handle button clicks
        self.buttonPlayPause.clicked.connect(onPlayPauseClick)
        self.buttonPreviousTrack.clicked.connect(onPreviousTrackClick)
        self.buttonNextTrack.clicked.connect(onNextTrackClick)

    # update GUI data
    def updateData(self, data):
        # set current track label
        self.labelCurrentTrack.setText(data['currentTrack'])
        # set current artist label
        self.labelCurrentArtist.setText(data['currentArtist'])
        # set previous track label
        self.labelPreviousTrack.setText(data['prevTrack'])
        # set previous artist label
        self.labelPreviousArtist.setText(data['prevArtist'])
        # store previous track for reference
        prevTrack = data['prevTrack']
        # if the track has been changed and it is not the first iteration
        if prevTrack not in trackHistory and len(prevTrack) > 0:
            # add track to track history
            trackHistory.append(prevTrack)
            # add track to list widget in GUI
            self.listTrackHistory.addItem(data['prevArtist'] + " - " + prevTrack)
        # create image object to store cover art
        coverArtImage = QImage()
        # load in image from given URL
        coverArtImage.loadFromData(requests.get(data['coverArt']).content)
        # convert to pixmap
        pixmap = QPixmap(coverArtImage)
        # scale it to fit GUI
        scaledPixmap = pixmap.scaledToHeight(180)
        # update GUI with cover art
        self.labelCoverArt.setPixmap(scaledPixmap)
        # update track popularity bar
        self.trackPopularity.setValue(data['trackPopularity'])
        # update timer
        self.labelTime.setText(data['timeString'])

# HANDLE BUTTON CLICKS
# play/pause
def onPlayPauseClick():
    handler.playPause()
# previous track
def onPreviousTrackClick():
    handler.previousTrack()
# next track
def onNextTrackClick():
    handler.nextTrack()

# run application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


