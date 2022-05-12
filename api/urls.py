from django.urls import path
from api.views import ShortURL

urlpatterns = [
    path("short-url/", ShortURL.as_view()),
    # path("", OriginalURL.as_view()),
]
