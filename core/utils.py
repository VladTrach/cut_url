from django.conf import settings
from django.utils.crypto import get_random_string

from core import models


def random_shortcut():
    shortcut_length = settings.SHORTCUT_LENGTH
    if shortcut_length:
        return get_random_string(length=shortcut_length)
    raise ValueError("Provided bad environment variable SHORTCUT_LENGTH")


def get_full_url(shortcut: str) -> str:
    shortcuts = models.UrlShortcut.objects.filter(shortcut=shortcut)
    if len(shortcuts) > 0:
        return shortcuts[0].full_url


def get_shortcut_by_id(pk: int) -> str:
    shortcuts = models.UrlShortcut.objects.filter(pk=pk)
    if len(shortcuts) > 0:
        return shortcuts[0].shortcut
