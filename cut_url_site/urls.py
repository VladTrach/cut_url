from django.urls import path

from cut_url_site.views import ShortcutRedirect, NewShortcutFormView, \
    ShortcutView

urlpatterns = [
    path('', NewShortcutFormView.as_view()),
    path('<shortcut>', ShortcutRedirect.as_view()),
    path('shortcut/<int:pk>', ShortcutView.as_view(), name='site-shortcut')
]
