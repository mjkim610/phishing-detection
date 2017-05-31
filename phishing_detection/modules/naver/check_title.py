# -*- coding: utf-8 -*-
from .. import get_root_domain

def check_title(url, resp):
    mod = 'check_title'
    correct_title = ["네이버 : 로그인", "Naver Sign in", "NAVER 登录", "NAVER 登入"]
    body = resp.text
    title = body.split('title>')
    current_title = ""
    if len(title) > 1:
        current_title = title[1][:-2]
    if isinstance(current_title, unicode):
        correct_title = [title.decode('utf-8') for title in correct_title]
    if current_title in correct_title:
        if get_root_domain(url) != 'naver.com':
            print get_root_domain(url)
            return "P", mod
        else:
            return "S", mod

    return "U", mod
