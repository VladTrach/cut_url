from django.db import models

from core.utils import random_shortcut


class UrlShortcut(models.Model):
    full_url = models.URLField()
    shortcut = models.CharField(
        max_length=30,
        blank=True,
        default=random_shortcut,
        unique=True,
    )
