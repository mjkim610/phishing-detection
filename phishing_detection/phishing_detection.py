import sys
import requests
from integrate import integrate

########
# Usage
# python phishing_detection.py [url]
########

DEFAULT_URL = 'http://www.naver.com/'

if __name__ == '__main__':
    url = DEFAULT_URL
    if len(sys.argv) > 1:
        url = sys.argv[1]
    try:
        result = integrate(url)
        print("Checking: " + url)
        print("Result: " + result)
    except:
        print("Error has occurred.")
    print('-----Terminating.-----')
