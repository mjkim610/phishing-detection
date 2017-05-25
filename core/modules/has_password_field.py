# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


# 정상적인 사이트에서도 로그인일 경우엔 무조건 password field가 있을테니
# 이 함수는 password field가 없을 경우 바로 phishing site가 아닌 것으로
# 간주하기 위해 사용할 수 있을 것 같습니다
def has_password_field(resp):
    mod = 'has_password_field'
    answer = "U"

    current_page = BeautifulSoup(resp.text, 'lxml')
    password_field = current_page.find_all('input', type="password")

    if len(password_field) == 0:
        answer = "S"

    return answer, mod
