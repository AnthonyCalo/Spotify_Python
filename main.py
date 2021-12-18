import requests
import base64
import json
from secrets import *

from requests.models import Response





authUrl="https://accounts.spotify.com/api/token"

authHeader={}
authData={}

clientId=clientId
clientSecret=clientSecret
#base 64 encode cliet id and client secret

def get_access_token(authUrl=authUrl):
    message=f"{clientId}:{clientSecret}"
    message_bytes=message.encode('ascii')
    base64_bytes=base64.b64encode(message_bytes)
    base64_messages=base64_bytes.decode('ascii')

    authHeader['Authorization']="Basic " + base64_messages
    authData['grant_type']="client_credentials"

    res = requests.post(authUrl, headers=authHeader, data=authData)

    resObject=res.json()
    access_token = resObject['access_token']
    return access_token
token = get_access_token()

playlistID="37i9dQZF1DXbJMiQ53rTyJ?si=33bda072f66449e5"



def getTracks(token=token,playlistID=playlistID):
    header={
        "Authorization": "Bearer " + token,
        "Content-Type": 'application/json'
    }
    res = requests.get(f"https://api.spotify.com/v1/playlists/{playlistID}", headers=header)
    resObject=res.json()
    return resObject


trackList=getTracks()

tracks= trackList['tracks']['items']
with open("songs_list.txt", "w") as f:
    for i in tracks:
        f.write("-----------------------------------\n")
        f.write("Artists: ")
        for artist in i['track']['artists']:
            f.write(artist['name'] + ", ")
        f.write("\n")
        f.write("Song Title: {}".format(i['track']['name']))
        f.write("\n")
        f.write("\n")
        f.write("\n")




