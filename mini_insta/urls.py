# File: mini_insta/urls.py
# Author: David Myat (amyat@bu.edu), 9/25/2025
# Description: URL routing for mini_insta project

from django.conf import settings
from django.urls import path

from . import views
from .views import ShowAllView

# URL pattern specific to the restaurant app
urlpatterns = [
    path("", ShowAllView.as_view(), name="show_all"),
]
