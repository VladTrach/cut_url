from django.urls import path

from api.views import FullUrl

urlpatterns = [
    path('get_full_url/', FullUrl.as_view())
]
