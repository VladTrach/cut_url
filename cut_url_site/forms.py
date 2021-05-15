from django import forms

from core.models import UrlShortcut


class NewShortcutForm(forms.ModelForm):

    class Meta:
        model = UrlShortcut
        fields = ('full_url', )
