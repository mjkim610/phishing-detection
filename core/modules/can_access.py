import requests

def can_access(url):
    try:
        current_page = (requests.get(url).text, 'lxml')
        answer = "SL"
    except requests.exceptions.ConnectionError:
        answer = "PL"
    return answer