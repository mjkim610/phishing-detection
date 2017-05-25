from modules.url_check import url_name_check
from modules.can_access import can_access
from modules.count_numOfdot import numOfdot
from modules.has_password_field import has_password_field
from modules.is_masquerading import is_masquerading

def integrate(url):
    result = "U"

    r = can_access(url)
    if r != "U":
        r = has_password_field(url)
        if r != "U":
            return r
    r = url_name_check(url)
    if r != "U":
        return r
    r = is_masquerading(url)
    if r != "U":
        return r
    r = numOfdot(url)
    if r != "U":
        return r
    return result
