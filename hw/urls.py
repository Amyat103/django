# file: hw/urls.py

from django.conf import settings
from django.urls import path

from . import views

# URL patterns specific for the hw app
urlpatterns = [
    # path(r"", views.home, name="home"),
    path(r"", views.home_page, name="home_page"),
    path(r"about", views.about, name="about_page"),
]
