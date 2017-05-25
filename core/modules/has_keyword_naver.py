def has_keyword_naver(url):
    if "naver.com" in url:
        answer = "SL"
    else:
        answer = "PL"
    return answer