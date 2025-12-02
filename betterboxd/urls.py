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
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("movie/<int:movie_id>/", views.movie_detail, name="movie_detail"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="betterboxd/login.html"),
        name="login",
    ),
]
