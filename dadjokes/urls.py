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
    path("joke/<int:index>/", views.index_joke, name="index_joke"),
    path("pictures/", views.show_all_pictures, name="pictures"),
    path("picture/<int:index>/", views.index_picture, name="index_picture"),
    path("api/", views.random, name="random_joke"),
    path("api/random/", views.random, name="random_joke"),
    path("api/jokes/", views.show_all_jokes, name="jokes"),
    path("api/joke/<int:index>/", views.index_joke, name="index_joke"),
    path("api/pictures/", views.show_all_pictures, name="pictures"),
    path("api/picture/<int:index>/", views.index_picture, name="index_picture"),
]
