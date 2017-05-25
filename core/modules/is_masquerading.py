DOMAIN_LIST = ["naver", "daum", "dcinside", "nate", ]

def is_masquerading(url):
    for domain_keyword in DOMAIN_LIST:
        if domain_keyword in url:
            domain = get_domain(url)
            if domain_keyword in domain:
                return "S"
            else:
                return "P"
        else:
            return "U"

def get_domain(url):
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

    return domain