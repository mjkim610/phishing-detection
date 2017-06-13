import sys
import requests
import socket

def can_access(url):
    mod = 'can_access'
    answer = "U"
    response = None
    try:
        response = requests.get(url, timeout=5)
        answer = "SL"
    except:
        print (sys.exc_info()[0])

    """
    except requests.exceptions.ConnectionError as e:
        print e
    except requests.exceptions.Timeout as e:
        print e
    except requests.TooManyRedirects as e:
        print e
    except requests.exceptions.ChunkedEncodingError as e:
        print e
    except requests.exceptions.ContentDecodingError as e:
        print e
    except socket.error as e:
        print e
    """
    return answer, response, mod
