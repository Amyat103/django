# File: mini_insta/urls.py
# Author: David Myat (amyat@bu.edu), 9/25/2025
# Description: URL routing for mini_insta project

from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import *  # ProfileDetailView, ProfileListView

# URL pattern specific to the restaurant app
urlpatterns = [
    path("", ProfileListView.as_view(), name="show_all_profiles"),
    path("profile/", ProfileDetailView.as_view(), name="profile"),
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name="show_profile"),
    path("profile/update", UpdateProfileView.as_view(), name="update_profile"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="show_post"),
    path(
        "profile/create_post/",
        views.CreatePostView.as_view(),
        name="create_post",
    ),
    path("post/<int:pk>/update", UpdatePostView.as_view(), name="update_post"),
    path("post/<int:pk>/delete", DeletePostView.as_view(), name="delete_post"),
    path(
        "profile/<int:pk>/followers",
        ShowFollowersDetailView.as_view(),
        name="show_followers",
    ),
    path(
        "profile/<int:pk>/following",
        ShowFollowingDetailView.as_view(),
        name="show_following",
    ),
    path("profile/feed", PostFeedListView.as_view(), name="show_feed"),
    path("profile/search", SearchView.as_view(), name="search"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="mini_insta/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="show_all_profiles"),
        name="logout",
    ),
    path("create_profile/", views.CreateProfileView.as_view(), name="create_profile"),
    path("profile/<int:pk>/follow", FollowView.as_view(), name="follow_profile"),
    path("profile/<int:pk>/unfollow", UnfollowView.as_view(), name="unfollow_profile"),
    path("post/<int:pk>/like", LikeView.as_view(), name="like_post"),
    path("post/<int:pk>/unlike", UnlikeView.as_view(), name="unlike_post"),
    path("post/<int:pk>/comment", PostDetailView.as_view(), name="add_comment"),
]
