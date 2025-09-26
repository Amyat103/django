# File: mini_insta/views.py
# Author: David Myat (amyat@bu.edu), 9/25/2025
# Description: Views for the mini_insta project
import random

from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Profile


# Create your views here.
class ProfileListView(ListView):
    """Define a view class to show all profiles"""

    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"


class ProfileDetailView(DetailView):
    """Display a single profile."""

    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"
