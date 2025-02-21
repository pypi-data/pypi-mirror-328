""" Utility functions """

def to_millis(x):
    return round(x * 1000)


def status(is_ok, is_optional):
    if is_ok:
        return "ok"
    elif is_optional:
        return "warn"
    else:
        return "fail"


def total_status(checks):

    if all(map(lambda check: check.get("status") == "ok", checks)):
        return 200, "ok"

    if any(map(lambda check: check.get("status") == "fail", checks)):
        return 500, "fail"

    return 400, "warn"
