import json
from firebase import firebase
import requests as req
def getUrl(url):
    firebase_url = 'https://freegamediscord-4d347-default-rtdb.asia-southeast1.firebasedatabase.app/'
    fdb = firebase.FirebaseApplication(firebase_url, None)
    last_url = fdb.get('/','data')
    res = req.get(url)
    data = json.loads(res.text)
    urlPush = data["data"]["results"][0]["canonicalUrl"]
    counter = 0
    if urlPush == last_url:
        print("Nothing to print")
    while urlPush != last_url:
        print(urlPush)
        counter += 1
        urlPush = data["data"]["results"][counter]["canonicalUrl"]
    fdb.put('/','data',data["data"]["results"][0]["canonicalUrl"])
