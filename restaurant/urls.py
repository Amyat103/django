# File: restaurant/urls.py
# Author: David Myat (amyat@bu.edu), 9/9/2025
# Description: URL routing for restaurant project

from django.conf import settings
from django.urls import path

from . import views

# URL pattern specific to the restaurant app
urlpatterns = [
    path(r"", views.main, name="main_page"),
    path(r"main/", views.main, name="main_page"),
    path(r"order/", views.order, name="order_page"),
    path(r"submit/", views.submit, name="submit"),
    path(r"confirmation/", views.confirmation, name="confirmation_page"),
]
