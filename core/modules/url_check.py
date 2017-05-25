def is_naver_domain(url):
    print('is_naver_domain')
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

    if domain == "naver.com":
        answer = "SL"
    else:
        answer = "U"

    return answer


def url_name_check(url):
    print('url_name_check')
    status = "U"
    url = url.rstrip()

    if url[0:7].find("https") == 1:
        status = "SL"

    if url.find("@") != -1:
        status = "P"

    if len(url) >= 75:
        status = "P"

    if url[7:].find("//") != -1 :
        status = "P"

    if url[7:].find("http") != -1 :
        status = "P"

    return status
