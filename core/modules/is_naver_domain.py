def is_naver_domain(url):
    temp = url.index("/")
    try:
        temp = url[temp + 2:].index("/") + temp + 2
    except:
        temp = len(url) + temp + 2

    url_parsed = url[:temp]
    domain_end = temp

    temp = url_parsed.rfind('.')
    domain_start = url_parsed[:temp].rfind('.')
    if domain_start == -1:
        domain_start = url_parsed[:temp].rfind('/')
    domain = url[domain_start + 1:domain_end]
    print(domain)

    if domain == "naver.com":
        answer = "SL"
    else:
        answer = "PL"
    return answer