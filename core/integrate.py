from modules.url_check import *
from modules.can_access import can_access
from modules.count_numOfdot import numOfdot


def integrate(url):
    result = "U"

    r = url_name_check(url)
    if r != "U":
        return r
    r = is_naver_domain(url)
    if r != "U":
        return r
    r = numOfdot(url)
    if r != "U":
        return r
    r = can_access(url)
    if r != "U":
        return r
    return result
