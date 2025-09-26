# File: mini_insta/views.py
# Author: David Myat (amyat@bu.edu), 9/25/2025
# Description: Views for the mini_insta project
import random

from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Profile


# Create your views here.
class ShowAllView(ListView):
    """Define a view class to show all profiles"""

    model = Profile
    template_name = "mini_insta/show_all.html"
    context_object_name = "profiles"


class ProfileView(DetailView):
    """Display a single profile."""

    model = Profile
    template_name = "mini_insta/profile.html"
    context_object_name = "profile"


class RandomProfileView(DetailView):
    """Display a single random profile."""

    model = Profile
    template_name = "mini_insta/random_profile.html"
    context_object_name = "profile"

    # method
    def get_object(self):
        """return one of the profile at random."""

        all_profiles = Profile.objects.all()
        profile = random.choice(all_profiles)
        return profile
