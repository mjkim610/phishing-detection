from bs4 import BeautifulSoup

"""
Sites that are in the Naver domain are already checked by is_masquerading. So no need to check url again
"""
def uses_stylesheet_naver(resp):
    mod = 'uses_stylesheet_naver'
    answer = "U"

    current_page = BeautifulSoup(resp.text, 'lxml')
    stylesheets = current_page.find_all('link', rel="stylesheet")

    for stylesheet in stylesheets:
        if "naver.com" in stylesheet['href']:
            return "P", mod
    return answer, mod
