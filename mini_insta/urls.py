# File: mini_insta/urls.py
# Author: David Myat (amyat@bu.edu), 9/25/2025
# Description: URL routing for mini_insta project

from django.conf import settings
from django.urls import path

from . import views
from .views import *  # ProfileDetailView, ProfileListView

# URL pattern specific to the restaurant app
urlpatterns = [
    path("", ProfileListView.as_view(), name="show_all_profiles"),
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name="profile"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="show_post"),
    path(
        "profile/<int:pk>/create_post/",
        views.CreatePostView.as_view(),
        name="create_post",
    ),
    path("post/<int:pk>/update", UpdatePostView.as_view(), name="update_post"),
    path("post/<int:pk>/delete", DeletePostView.as_view(), name="delete_post"),
]
