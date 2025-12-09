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
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
    path("movie/create/", CreateMovieView.as_view(), name="create_movie"),
    path(
        "movie/<int:pk>/review/create", CreateReviewView.as_view(), name="create_review"
    ),
    path(
        "movie/<int:pk>/update/",
        UpdateReviewView.as_view(),
        name="update_review",
    ),
    path(
        "movie/<int:pk>/delete/",
        DeleteReviewView.as_view(),
        name="delete_review",
    ),
    path(
        "movie/<int:pk>/watchlist/add/", views.addToWatchlist, name="add_to_watchlist"
    ),
    path(
        "movie/<int:pk>/watchlist/remove/",
        views.removeFromWatchlist,
        name="remove_from_watchlist",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="betterboxd/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="show_all_movies"),
        name="logout",
    ),
    path("register/", CreateUserView.as_view(), name="create_user"),
    path("watchlist/", ShowWatchlistView.as_view(), name="watchlist"),
]
