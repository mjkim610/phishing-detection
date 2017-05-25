from modules.naver import main
from modules.can_access import can_access
from modules.has_keyword_naver import has_keyword_naver
from modules.is_naver_domain import is_naver_domain


def integrate(url):
    result = main(url)
    # result = can_access(url)
    print url, result
    # result = has_keyword_naver(url)
    # result = is_naver_domain(url)
    return result
