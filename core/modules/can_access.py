import requests


def can_access(url):
    print('can_access')
    answer = "U"
    try:
        current_page = (requests.get(url, timeout=3).text, 'lxml')
        answer = "SL"
    except requests.exceptions.ConnectionError:
        print("ERROR: Page is inaccessible, return U and move to next case.")
    except requests.exceptions.Timeout as e:
        print e
    except requests.TooManyRedirects as e:
        print e
    return answer