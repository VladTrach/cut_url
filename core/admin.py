from django.contrib import admin

from core.models import UrlShortcut


class UrlShortcutAdmin(admin.ModelAdmin):
    pass


admin.site.register(UrlShortcut, UrlShortcutAdmin)
