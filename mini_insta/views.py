# File: mini_insta/views.py
# Author: David Myat (amyat@bu.edu), 9/25/2025
# Description: Views for the mini_insta project
import random

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import *

from .forms import CreatePostForm, UpdatePostForm, UpdateProfileForm
from .models import *


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

    def get_success_url(self):
        """Provide a URL to redirect to after successfully creating a post."""
        return reverse("show_post", kwargs={"pk": self.object.pk})

    def get_context_data(self):
        """return context data for the template."""
        context = super().get_context_data()

        pk = self.kwargs["pk"]
        profile = Profile.objects.get(pk=pk)
        context["profile"] = profile

        return context

    def form_valid(self, form):
        """handle form submission if form is valid."""
        pk = self.kwargs["pk"]
        profile = Profile.objects.get(pk=pk)
        form.instance.profile = profile
        self.object = form.save()

        # if there is image url in creation make object and save
        files = self.request.FILES.getlist("image_file")
        for file in files:
            photo = Photo(post=self.object, image_file=file)
            photo.save()

        return super().form_valid(form)


class PostDetailView(DetailView):
    """Display a single post."""

    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"


class UpdatePostView(UpdateView):
    """A view to handle updating an existing post."""

    model = Post
    form_class = UpdatePostForm
    template_name = "mini_insta/update_post_form.html"

    def get_success_url(self):
        """Provide a URL to redirect to after successfully updating a post."""
        return reverse("show_post", kwargs={"pk": self.object.pk})


class DeletePostView(DeleteView):
    """A view to handle deleting an existing post."""

    model = Post
    template_name = "mini_insta/delete_post_form.html"

    def get_success_url(self):
        """Return the URL to redirect to after deleting a post."""

        pk = self.kwargs["pk"]
        post = Post.objects.get(pk=pk)

        profile_pk = post.profile.pk

        return reverse("profile", kwargs={"pk": profile_pk})


class UpdateProfileView(UpdateView):
    """A view to handle updating an existing profile."""

    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"


class ShowFollowersDetailView(DetailView):
    """Display a single profile's followers."""

    model = Profile
    template_name = "mini_insta/show_followers.html"

    def get_context_data(self):
        """return context data for the template."""
        context = super().get_context_data()

        pk = self.kwargs["pk"]
        profile = Profile.objects.get(pk=pk)
        context["profile"] = profile

        followers = profile.get_follower()
        context["followers"] = followers

        return context


class ShowFollowingDetailView(DetailView):
    """Display a single profile's following."""

    model = Profile
    template_name = "mini_insta/show_following.html"

    def get_context_data(self):
        """return context data for the template."""
        context = super().get_context_data()

        pk = self.kwargs["pk"]
        profile = Profile.objects.get(pk=pk)
        context["profile"] = profile

        following = profile.get_following()
        context["following"] = following

        return context
