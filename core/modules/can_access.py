import requests

def can_access(url):
    try:
        current_page = (requests.get(url).text, 'lxml')
        answer = "SL"
    except requests.exceptions.ConnectionError:
        print("ERROR: Page is inaccessible, return U and move to next case.")
        answer = "U"
    return answer