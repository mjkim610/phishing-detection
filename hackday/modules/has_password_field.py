from bs4 import BeautifulSoup

def has_password_field(resp):
    mod = 'has_password_field'
    answer = "U"

    current_page = BeautifulSoup(resp.text, 'lxml')
    password_field = current_page.find_all('input', type="password")

    if len(password_field) == 0:
        answer = "S"

    return answer, mod
