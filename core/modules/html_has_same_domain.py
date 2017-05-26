from bs4 import BeautifulSoup as bs
from get_root_domain import get_root_domain


def html_has_same_domain(url, resp):
    mod = 'html_has_same_domain'
    cnt = 0
    root = get_root_domain(url)

    current_page = bs(resp.text, 'lxml')
    for tag in current_page.find_all('a'):
        if tag.get('href'):
            in_url = get_root_domain(tag.get('href'))
            if in_url == root:
                cnt += 1

    if cnt >= 1:
        return "S", mod
    return "U", mod
