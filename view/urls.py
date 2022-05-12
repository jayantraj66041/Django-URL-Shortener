from django.urls import path
from view.views import UrlShortView, LongUrlView, AboutUs


urlpatterns = [
    path("", UrlShortView.as_view(), name="homepage"),
    path("aboutus/", AboutUs.as_view(), name="aboutus"),
    path("<str:token>/", LongUrlView.as_view()),
]
