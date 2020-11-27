import os
import json
import sys
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

#get the username from terminal
username = sys.argv[1]
#USER ID : https://open.spotify.com/user/divi99?si=MO0WebK2Slum7q2YGU4HCA

#erase cache and prompt user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f'.cache-(username)')
    token = util.prompt_for_user_token(username)

#Create our SpotifyObject
SpotifyObject = spotipy.Spotify(auth=token)

user = SpotifyObject.current_user()
print(json.dumps(user, sort_keys=True, indent=4))

#print(json.dumps(VARIABLE, sort_keys=True, indent=4))

