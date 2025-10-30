# File: voter_analytics/urls.py
# Author: David Myat (amyat@bu.edu), 10/28/2025
# Description: URL routing for voter_analytics project

from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import *

# URL pattern specific to the voter_analytics app
urlpatterns = [
    path("", VoterListView.as_view(), name="show_all_voters"),
    path("voter/<int:pk>/", VoterDetailView.as_view(), name="voter"),
]
