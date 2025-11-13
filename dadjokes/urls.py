# File: dadjokes/urls.py
# Author: David Myat (amyat@bu.edu), 11/13/2025
# Description: URL routing for dadjokes project

from django.urls import path

from . import views

# URL pattern specific to the restaurant app
urlpatterns = [
    path("", views.show_random, name="random"),
    path("random/", views.show_random, name="random_page"),
    path("jokes/", views.show_all_jokes, name="jokes"),
    path("joke/<int:index>/", views.index_joke, name="joke_detail"),
    path("pictures/", views.show_all_pictures, name="pictures"),
    path("picture/<int:index>/", views.index_picture, name="picture_detail"),
    path("api/", views.api_random_joke, name="api_random"),
    path("api/random/", views.api_random_joke, name="api_random_alt"),
    path("api/jokes/", views.JokeListAPIView.as_view(), name="api_jokes"),
    path(
        "api/joke/<int:pk>/", views.JokeDetailAPIView.as_view(), name="api_joke_detail"
    ),
    path("api/pictures/", views.PictureListAPIView.as_view(), name="api_pictures"),
    path(
        "api/picture/<int:pk>/",
        views.PictureDetailAPIView.as_view(),
        name="api_picture_detail",
    ),
    path("api/random_picture/", views.api_random_picture, name="api_random_picture"),
]
