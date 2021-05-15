from django.conf import settings
from django.utils.crypto import get_random_string


def random_shortcut():
    shortcut_length = settings.SHORTCUT_LENGTH
    if shortcut_length:
        return get_random_string(length=shortcut_length)
    raise ValueError("Provided bad environment variable SHORTCUT_LENGTH")
