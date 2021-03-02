import spotipy
import sys
import spotipy.util as util
import time
from spotipy.oauth2 import SpotifyOAuth

class APImanager:
    def __init__(self):
        scope = "user-read-currently-playing user-read-playback-state user-read-playback-position user-follow-read"

        username = 'OctaneMR'
        SPOTIPY_CLIENT_ID='70556e1830db4dd687adce562f4b9124'
        SPOTIPY_CLIENT_SECRET='b6d2a399476e496ba1f27fd7bdbd0c4f'
        SPOTIPY_REDIRECT_URI='http://localhost/'

        token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
        self.sp = spotipy.Spotify(auth=token)


    def getPlaying(self):
        results = self.sp.current_playback()
        track = results['item']
        # print(track['artists'][0]['name'])
        return track['name']
        # time.sleep(3)


    
