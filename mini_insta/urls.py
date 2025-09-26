# File: mini_insta/urls.py
# Author: David Myat (amyat@bu.edu), 9/25/2025
# Description: URL routing for mini_insta project

from django.conf import settings
from django.urls import path

from . import views
from .views import ProfileView, ShowAllView

# URL pattern specific to the restaurant app
urlpatterns = [
    path("", ShowAllView.as_view(), name="show_all"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
]
