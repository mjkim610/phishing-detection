import sys
import requests
from integrate import integrate

########
# Usage
# python sample.py [key]
########

URL = 'http://220.230.122.163/'
START = 'api/start'
STOP = 'api/stop'
SUBMIT = 'api/submit'
STATUS = 'api/status'
KEY = 'user_dog'


def start():
    res = requests.post(URL+START, json={'key': KEY, 'type': "N"})
    print('start', res.status_code)
    url = res.json()['url']

    while True:
        print(url)
        answer = integrate(url)
        print(answer)
        res = requests.post(URL+SUBMIT, json={'key': KEY, 'answer': answer})
        left = res.json()[u'left']
        url = res.json()[u'url']
        if left <= 1:
            requests.post(URL+SUBMIT, json={'key': KEY, 'answer': answer})
            break

        if left % 100 == 0:
            print(left)

    res = requests.get(URL+STATUS, {'key': KEY})
    print('status', res.status_code)
    print(res.text)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        KEY = sys.argv[1]
    try:
        start()
    except ValueError as e:
        print(e)
        print('value error!')
        res = requests.post(URL+STOP, json={'key': KEY})
        print('stop', res.status_code)
    except requests.exceptions.RequestException as e:
        print(e)
        print('request error!')
        res = requests.post(URL+STOP, json={'key': KEY})
        print('stop', res.status_code)
    except AttributeError as e:
        print(e)
        print('attribute error error!')
        res = requests.post(URL+STOP, json={'key': KEY})
        print('stop', res.status_code)

    print('end!')
