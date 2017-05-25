import requests

URL = 'http://220.230.122.163/'
START = 'api/start'
STOP = 'api/stop'
SUBMIT = 'api/submit'
STATUS = 'api/status'
KEY = 'user_fish'


def something(url):
    if len(url) > 100:
        answer = "P"
    else:
        answer = "U"
    return answer


try:
    res = requests.post(URL+START, json={'key': KEY, 'type': "N"})
    print('start', res.status_code)
    left = res.json()['left']
    url = res.json()['url']

    while True:
        answer = something(url)
        res = requests.post(URL+SUBMIT, json={'key': KEY, 'answer': answer})
        left = res.json()[u'left']
        url = res.json()[u'url']
        if left <= 1:
            res = requests.post(URL+SUBMIT, json={'key': KEY, 'answer': answer})
            break

        if left % 100 == 0:
            print(left)

    res = requests.get(URL+STATUS, {'key': KEY})
    print('status', res.status_code)
    print(res.text)

except:
    print('error!')


res = requests.post(URL+STOP, json={'key': KEY})
print('stop', res.status_code)
