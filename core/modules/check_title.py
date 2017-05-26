# -*- coding: utf-8 -*-
from html_has_same_domain import get_root_domain


def check_title(url, resp):
    mod = 'check_title'
    correct_title = ["네이버 : 로그인", "Naver Sign in", "NAVER 登录", "NAVER 登入"]
    body = resp.text
    title = body.split('title>')
    current_title = title[1][:-2]
    if current_title in correct_title:
        if get_root_domain(url) != 'naver.com':
            print get_root_domain(url)
            return "P", mod

    return "U", mod
