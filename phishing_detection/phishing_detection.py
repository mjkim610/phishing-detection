import sys
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
        integrate(url)
    except:
        print("Error has occurred.")
    print('----------Terminating----------')
