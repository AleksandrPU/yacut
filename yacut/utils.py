from random import choices
from string import ascii_letters, digits

from .constants import LENGTH_GENERATE_CUSTOM_ID
from .models import URLMap


def get_unique_short_id():
    while True:
        custom_id = ''.join(
            choices(ascii_letters + digits, k=LENGTH_GENERATE_CUSTOM_ID)
        )
        if URLMap.query.filter_by(short=custom_id).first() is None:
            break
    return custom_id
