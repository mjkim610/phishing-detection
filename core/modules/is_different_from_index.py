from bs4 import BeautifulSoup
import requests

def is_different_from_index(url, resp):
    mod = 'uses_stylesheet_naver'
    answer = "U"

    try:
        current_page = BeautifulSoup(resp.text, 'lxml')
        meta_tag = current_page.find('meta')
        url_attrs = meta_tag.attrs

        temp = url.index("/")
        try:
            temp = url[temp + 2:].index("/") + temp + 2
        except:
            temp = len(url) + temp + 2

        domain_url = url[:temp]

        response = requests.get(domain_url, timeout=3)
        index_page = BeautifulSoup(response.text, 'lxml')
        meta_tag = index_page.find('meta')
        domain_attrs = meta_tag.attrs

        print(url_attrs)
        print(domain_attrs)

        if (url_attrs != domain_attrs):
            return "P", mod
    except:
        print("Cannot get meta tag")
    return answer, mod
