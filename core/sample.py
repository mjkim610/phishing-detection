import requests

URL = 'http://220.230.122.163/'
START = 'api/start'
STOP = 'api/stop'
KEY = 'user_fish'

res = requests.post(URL+START, json={'key': KEY, 'type': "N"})
print(res.text)