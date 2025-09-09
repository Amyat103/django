# File: quotes/urls.py
# Author: David Myat (amyat@bu.edu), 9/9/2025
# Description: URL routing for quotes project

from django.conf import settings
from django.urls import path

from . import views

# URL pattern specific to the quotes app
urlpatterns = [
    path(r"", views.home, name="home"),
    path(r"quotes/", views.quotes, name="quotes"),
    path(r"show_all/", views.show_all, name="show_all"),
    path(r"about/", views.about, name="about"),
]
