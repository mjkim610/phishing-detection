def url_name_check(url):
    print('url_name_check')
    status = "U"
    url = url.rstrip()

    if url[0:7].find("https") == 1:
        return "S"

    if url.find("@") != -1:
        return "P"

    if len(url) >= 75:
        return "P"

    if url[7:].find("//") != -1 :
        return "P"

    if url[7:].find("http") != -1 :
        return "P"

    return status
