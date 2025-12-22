def safe_str(obj):
    try:
        return str(obj)
    except Exception:
        return repr(obj)


def extract_exception_name(exc_type):
    try:
        return f"{exc_type.__module__}.{exc_type.__name__}"
    except AttributeError:
        return str(exc_type)


def truncate_message(msg, max_length=120):
    msg = str(msg)
    if len(msg) > max_length:
        return msg[:max_length] + "..."
    return msg


def last_frame(frames):
    if not frames:
        return None
    return frames[-1]


def first_frame(frames):
    if not frames:
        return None
    return frames[0]
