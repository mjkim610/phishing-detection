from modules.check_title import check_title
from modules.can_access import can_access
from modules.has_password_field import has_password_field
from modules.is_masquerading import is_masquerading
from modules.html_has_same_domain import html_has_same_domain
from modules.uses_stylesheet_naver import uses_stylesheet_naver

def integrate(url):
    result = "U"

    r, mod = is_masquerading(url)
    if r != "U":
        print "Detect By ", mod
        return r

    r, resp, mod = can_access(url)
    if r != "U":
        r, mod = html_has_same_domain(url, resp)
        if r != "U":
            print "Detect By ", mod
            return r
        r, mod = has_password_field(resp)
        if r != "U":
            print "Detect By ", mod
            return r
        r, mod = uses_stylesheet_naver(resp)
        if r != "U":
            print "Detect By ", mod
            return r
        r, mod = check_title(url, resp)
        if r != "U":
            print "Detect By ", mod
            return r

    if result == "U":
        mod = "* Nothing! *"

    print "Detect By ", mod
    return result
