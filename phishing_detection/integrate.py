from modules.can_access import can_access
from modules.check_post_action import check_post_action
from modules.check_title import check_title
from modules.has_correct_favicon import has_correct_favicon
from modules.has_password_field import has_password_field
from modules.html_has_same_domain import html_has_same_domain
from modules.is_masquerading import is_masquerading
from modules.uses_stylesheet_naver import uses_stylesheet_naver

def finish_check(mod, result):
    print("Determined by:\t" + mod)
    print("Result:\t\t\t" + result)

def integrate(url):
    print("Checking:\t\t" + url)

    result = "U"

    result, mod = is_masquerading(url)
    if result != "U":
        finish_check(mod, result)
        return result

    result, resp, mod = can_access(url)
    if result != "U":
        result, mod = html_has_same_domain(url, resp)
        if result != "U":
            finish_check(mod, result)
            return result
        result, mod = has_password_field(resp)
        if result != "U":
            finish_check(mod, result)
            return result
        result, mod = uses_stylesheet_naver(resp)
        if result != "U":
            finish_check(mod, result)
            return result
        result, mod = check_title(url, resp)
        if result != "U":
            finish_check(mod, result)
            return result
        result, mod = has_correct_favicon(url, resp)
        if result != "U":
            finish_check(mod, result)
            return result
        result, mod = check_post_action(resp)
        if result != "U":
            finish_check(mod, result)
            return result
        finish_check("*Nothing*", result)
        return "S"

    result = "S"
    mod = "*Page inaccessible*"

    finish_check(mod, result)
    return result
