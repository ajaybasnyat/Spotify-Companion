import spotipy
import sys
import spotipy.util as util
import time
from spotipy.oauth2 import SpotifyOAuth


scope = "user-read-currently-playing user-read-playback-state user-read-playback-position user-follow-read"



username = 'OctaneMR'
SPOTIPY_CLIENT_ID='70556e1830db4dd687adce562f4b9124'
SPOTIPY_CLIENT_SECRET='b6d2a399476e496ba1f27fd7bdbd0c4f'
SPOTIPY_REDIRECT_URI='http://localhost/'

token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)

sp = spotipy.Spotify(auth=token)


# while True:
#     results = sp.current_playback()
#     track = results['item']
#     print(track['artists'][0]['name'])
#     print(": " + track['name'])
#     time.sleep(3)

result = sp.current_user_followed_artists(limit=50, after='1o2NpYGqHiCq7FoiYdyd1x')
artists = result['artists']['items']
for artist in artists:
    print(artist['name'])
    
