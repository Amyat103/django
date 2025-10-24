# File: mini_insta/views.py
# Author: David Myat (amyat@bu.edu), 9/25/2025
# Description: Views for the mini_insta project
import random
from multiprocessing import context

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import *

from .forms import CreatePostForm, CreateProfileForm, UpdatePostForm, UpdateProfileForm
from .models import *


# Create your views here.
class ProfileListView(ListView):
    """Define a view class to show all profiles"""

    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"

    def dispatch(self, request, *args, **kwargs):
        """Override the dispatch method to add debugging information."""

        print(f"user = {request.user}")
        return super().dispatch(request, *args, **kwargs)


class ProfileDetailView(DetailView):
    """Display a single profile."""

    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"

    def get_object(self):
        """Return profile of current logged in user."""
        if "pk" in self.kwargs:
            return Profile.objects.get(pk=self.kwargs["pk"])
        else:
            return Profile.objects.get(user=self.request.user)


class PostView(DetailView):
    """Display a single post."""

    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"


class CreatePostView(LoginRequiredMixin, CreateView):
    """A view to handle creation of a new post."""

    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_login_url(self):
        """Return URL for the app's login page."""

        return reverse("login")

    def get_success_url(self):
        """Provide a URL to redirect to after successfully creating a post."""
        return reverse("show_post", kwargs={"pk": self.object.pk})

    def get_context_data(self):
        """return context data for the template."""
        context = super().get_context_data()

        profile = Profile.objects.get(user=self.request.user)
        context["profile"] = profile

        return context

    def form_valid(self, form):
        """handle form submission if form is valid."""
        profile = Profile.objects.get(user=self.request.user)
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


class UpdatePostView(LoginRequiredMixin, UpdateView):
    """A view to handle updating an existing post."""

    model = Post
    form_class = UpdatePostForm
    template_name = "mini_insta/update_post_form.html"

    def get_success_url(self):
        """Provide a URL to redirect to after successfully updating a post."""
        return reverse("show_post", kwargs={"pk": self.object.pk})

    def get_login_url(self):
        """Return URL for the app's login page."""

        return reverse("login")


class DeletePostView(LoginRequiredMixin, DeleteView):
    """A view to handle deleting an existing post."""

    model = Post
    template_name = "mini_insta/delete_post_form.html"

    def get_success_url(self):
        """Return the URL to redirect to after deleting a post."""

        pk = self.kwargs["pk"]
        post = Post.objects.get(pk=pk)

        profile_pk = post.profile.pk

        return reverse("show_profile", kwargs={"pk": profile_pk})

    def get_login_url(self):
        """Return URL for the app's login page."""

        return reverse("login")


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """A view to handle updating an existing profile."""

    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"

    def get_login_url(self):
        """Return URL for the app's login page."""

        return reverse("login")

    def get_object(self):
        """Return profile of current logged in user."""

        return Profile.objects.get(user=self.request.user)


class ShowFollowersDetailView(DetailView):
    """Display a single profile's followers."""

    model = Profile
    template_name = "mini_insta/show_followers.html"

    def get_context_data(self, **kwargs):
        """return context data for the template."""
        context = super().get_context_data()

        pk = self.kwargs["pk"]
        profile = Profile.objects.get(pk=pk)
        context["profile"] = profile

        followers = profile.get_followers()
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


class PostFeedListView(LoginRequiredMixin, ListView):
    """Define a view class to show feed for a profile"""

    model = Post
    template_name = "mini_insta/show_feed.html"
    context_object_name = "posts"

    def get_queryset(self):
        """Return QuerySet of posts for this profile's feed."""
        profile = Profile.objects.get(user=self.request.user)
        posts = profile.get_post_feed()
        return posts

    def get_context_data(self, **kwargs):
        """Return context data for the template."""
        context = super().get_context_data(**kwargs)

        profile = Profile.objects.get(user=self.request.user)
        context["profile"] = profile

        return context

    def get_login_url(self):
        """Return URL for the app's login page."""

        return reverse("login")


class SearchView(LoginRequiredMixin, ListView):
    """Define a view class to search profiles and posts"""

    model = Post
    template_name = "mini_insta/search_results.html"
    context_object_name = "posts"

    def dispatch(self, request, *args, **kwargs):
        """Method to handle search form."""
        # if no query go to search form or err
        if "query" not in request.GET:
            profile = Profile.objects.get(user=self.request.user)
            context = {"profile": profile}
            return render(request, "mini_insta/search.html", context)
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """Return QuerySet of search."""
        query = self.request.GET.get("query")
        if query:
            posts = Post.objects.filter(caption__contains=query)
            return posts
        else:
            return Post.objects.none()

    def get_context_data(self, **kwargs):
        """Return context data for the template."""
        context = super().get_context_data(**kwargs)

        profile = Profile.objects.get(user=self.request.user)
        context["profile"] = profile

        query = self.request.GET.get("query")
        context["query"] = query

        if query:
            profiles = (
                Profile.objects.filter(username__contains=query)
                | Profile.objects.filter(display_name__contains=query)
                | Profile.objects.filter(bio_text__contains=query)
            )
            context["profiles"] = profiles
        else:
            context["profiles"] = Profile.objects.none()

        return context

    def get_login_url(self):
        """Return URL for the app's login page."""

        return reverse("login")


class CreateProfileView(CreateView):
    """A view to show/process the registration to create a new user."""

    form_class = CreateProfileForm
    template_name = "mini_insta/create_profile_form.html"
    model = Profile

    def get_context_data(self, **kwargs):
        """Return context data for the template."""
        context = super().get_context_data(**kwargs)

        if "user_form" not in context:
            context["user_form"] = UserCreationForm()

        return context

    def form_valid(self, form):
        """Handle a valid form submission."""
        user_form = UserCreationForm(self.request.POST)

        if user_form.is_valid():
            user = user_form.save()
            login(
                self.request, user, backend="django.contrib.auth.backends.ModelBackend"
            )
            form.instance.user = user

            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        """Provide a URL to redirect to after successfully registering a user."""
        return reverse("profile")


class LikeView(LoginRequiredMixin, View):
    """A view to handle liking a post."""

    def get_login_url(self):
        """Return URL for the login page."""

        return reverse("login")

    def dispatch(self, request, *args, **kwargs):
        """Handle like action."""
        pk = self.kwargs["pk"]
        post = Post.objects.get(pk=pk)

        profile = Profile.objects.get(user=self.request.user)

        if profile != post.profile:
            seen_like = Like.objects.filter(post=post, profile=profile)
            # like or unlike
            if not seen_like:
                Like.objects.create(post=post, profile=profile)

        return redirect("show_post", pk=pk)


class UnlikeView(LoginRequiredMixin, View):
    """A view to handle unliking a post."""

    def get_login_url(self):
        """Return URL for the login page."""

        return reverse("login")

    def dispatch(self, request, *args, **kwargs):
        """Handle unlike action."""
        pk = self.kwargs["pk"]
        post = Post.objects.get(pk=pk)

        profile = Profile.objects.get(user=self.request.user)

        if profile != post.profile:
            seen_like = Like.objects.filter(post=post, profile=profile)
            # unlike
            if seen_like:
                seen_like.delete()

        return redirect("show_post", pk=pk)


class FollowView(LoginRequiredMixin, View):
    """A view to handle following a profile."""

    def get_login_url(self):
        """Return URL for the login page."""

        return reverse("login")

    def dispatch(self, request, *args, **kwargs):
        """Handle follow action."""
        pk = self.kwargs["pk"]
        profile_to_follow = Profile.objects.get(pk=pk)

        logged_in = Profile.objects.get(user=self.request.user)

        if logged_in != profile_to_follow:
            seen_follow = Follow.objects.filter(
                profile=profile_to_follow, follower_profile=logged_in
            )
            if not seen_follow:
                Follow.objects.create(
                    profile=profile_to_follow, follower_profile=logged_in
                )

        return redirect("show_profile", pk=pk)


class UnfollowView(LoginRequiredMixin, View):
    """A view to handle unfollowing a profile."""

    def get_login_url(self):
        """Return URL for the login page."""

        return reverse("login")

    def dispatch(self, request, *args, **kwargs):
        """Handle unfollow action."""
        pk = self.kwargs["pk"]
        profile_to_unfollow = Profile.objects.get(pk=pk)

        logged_in = Profile.objects.get(user=self.request.user)

        if logged_in != profile_to_unfollow:
            seen_follow = Follow.objects.filter(
                profile=profile_to_unfollow, follower_profile=logged_in
            )
            if seen_follow:
                seen_follow.delete()

        return redirect("show_profile", pk=pk)
