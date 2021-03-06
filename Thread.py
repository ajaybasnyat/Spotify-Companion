from APIHandler import APIHandler
from PyQt5 import QtCore
from PyQt5.QtCore import *
import time

# create thread class for updating the GUI in live time
class Thread(QtCore.QThread):
    # create signal that the application can listen to
    # the type is dictionary so all data can be passed simultaneously by keys
    newData = pyqtSignal(dict)
    # create handler for managing api interactions
    handler = APIHandler()
    
    def __init__(self,):
        super(Thread, self).__init__()

    def run(self):
        # create data dictionary
        data = {}
        # intialize strings for storing current and previous track data
        previousTrack = ''
        recentTrack = ''
        previousArtist = ''
        recentArtist = ''

        # create timer string that is used to show session listening time
        timer = [0, 0, 0]
        pattern = '{0:02d}:{1:02d}:{2:02d}'
        timeString = '00:00:00'
        # loop endlessly for live updates
        while True:
            # use handler to get current data
            currentTrack = self.handler.getCurrentTrack()
            currentArtist = self.handler.getCurrentArtist()
            coverArt = self.handler.getCoverArt()
            trackPopularity = self.handler.getTrackPopularity()
            isPlaying = self.handler.isPlaying()
            # update previous and recent track history
            if currentTrack != recentTrack:
                previousTrack = recentTrack
                previousArtist = recentArtist
                recentTrack = currentTrack
                recentArtist = currentArtist
            # update timer if user is currently listening
            if isPlaying:
                timer[2] += 1
                if (timer[2] >= 60):
                    timer[2] = 0
                    timer[1] += 1
                if (timer[1] >= 60):
                    timer[0] += 1
                    timer[1] = 0
                timeString = pattern.format(timer[0], timer[1], timer[2])
            # assign data keys and values to be passed
            data['currentTrack'] = currentTrack
            data['currentArtist'] = currentArtist
            data['coverArt'] = coverArt
            data['prevArtist'] = previousArtist
            data['prevTrack'] = previousTrack
            data['trackPopularity'] = trackPopularity
            data['timeString'] = timeString
            # emit the data
            self.newData.emit(data)
            # repeat every second (so app does not exceed API rate limit)
            time.sleep(1)