# File: betterboxd/urls.py
# Author: David Myat (amyat@bu.edu), 11/24/2025
# Description: URL routing for betterboxd project

from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import *

# URL pattern specific to the betterboxd app
urlpatterns = [
    path("", ShowAllMovies.as_view(), name="show_all_movies"),
    path("movie/<int:pk>/", ShowMovieDetail.as_view(), name="movie_detail"),
    path("movie/create/", CreateMovieView.as_view(), name="create_movie"),
    path("movie/<int:pk>/review/", CreateReviewView.as_view(), name="create_review"),
    path(
        "movie/<int:pk>/review/update/",
        UpdateReviewView.as_view(),
        name="update_review",
    ),
    path(
        "movie/<int:pk>/review/delete/",
        DeleteReviewView.as_view(),
        name="delete_review",
    ),
]
