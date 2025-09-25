# File: mini_insta/views.py
# Author: David Myat (amyat@bu.edu), 9/25/2025
# Description: Views for the mini_insta project
from django.shortcuts import render
from django.views.generic import ListView

from .models import Profile


# Create your views here.
class ShowAllView(ListView):
    """Define a view class to show all profiles"""

    model = Profile
    template_name = "mini_insta/show_all.html"
    context_object_name = "profiles"
