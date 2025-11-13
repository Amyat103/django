# File: dadjokes/urls.py
# Author: David Myat (amyat@bu.edu), 11/13/2025
# Description: URL routing for dadjokes project

from django.urls import path

from . import views

# URL pattern specific to the restaurant app
urlpatterns = [
    path("", views.random, name="random_joke"),
    path("random/", views.random, name="random_joke"),
    path("jokes/", views.show_all_jokes, name="jokes"),
]
