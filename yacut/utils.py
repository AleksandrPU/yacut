from random import choices
from string import ascii_letters, digits

from yacut.models import URLMap


def get_unique_short_id():
    while True:
        custom_id = ''.join(choices(ascii_letters + digits, k=6))
        if URLMap.query.filter_by(short=custom_id).first() is None:
            break
    return custom_id
