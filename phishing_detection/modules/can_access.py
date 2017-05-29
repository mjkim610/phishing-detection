import requests
import socket

def can_access(url):
    mod = 'can_access'
    answer = "U"
    response = None
    try:
        response = requests.get(url, timeout=5)
        current_page = (response.text, 'lxml')
        answer = "SL"
    except requests.exceptions.ConnectionError:
        print("ERROR: Page is inaccessible, return U and move to next case.")
    except requests.exceptions.Timeout as e:
        print e
    except requests.TooManyRedirects as e:
        print e
    except requests.exceptions.ChunkedEncodingError as e:
        print e
    except socket.error as e:
        print e
    return answer, response, mod
