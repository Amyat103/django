# File: mini_insta/views.py
# Author: David Myat (amyat@bu.edu), 9/25/2025
# Description: Views for the mini_insta project
import random

from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from .forms import CreatePostForm
from .models import Post, Profile


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


class PostView(DetailView):
    """Display a single post."""

    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"


class CreatePostView(CreateView):
    """A view to handle creation of a new post."""

    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"


class PostDetailView(DetailView):
    """Display a single post."""

    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"
