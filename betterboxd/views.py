from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CreateMovieForm, CreateReviewForm, UpdateReviewForm
from .models import Movie, Review, Watchlist


# Create your views here.
class ShowAllMovies(ListView):
    """Function to respond to home request."""

    model = Movie
    template_name = "betterboxd/show_all_movies.html"
    context_object_name = "movie"

    def get_queryset(self):
        """Return the queryset of movies."""
        qs = super().get_queryset()

        title = self.request.GET.get("title")
        if title:
            qs = qs.filter(title__icontains=title)

        genre = self.request.GET.get("genre")
        if genre:
            qs = qs.filter(genre__icontains=genre)

        year = self.request.GET.get("year")
        if year:
            qs = qs.filter(year=year)

        return qs


class MovieDetailView(DetailView):
    """Function to respond to movie detail request."""

    model = Movie
    template_name = "betterboxd/movie_detail.html"
    context_object_name = "movie"

    def get_context_data(self, **kwargs):
        """Add reviews to data and check if movie is in user's watchlist."""

        context = super().get_context_data(**kwargs)
        context["reviews"] = self.object.review_set.all()

        if self.request.user.is_authenticated:
            in_watchlist = Watchlist.objects.filter(
                user=self.request.user, movie=self.object
            ).exists()
            context["is_in_watchlist"] = in_watchlist

        return context


class CreateMovieView(CreateView):
    """View to create a new movie."""

    model = Movie
    form_class = CreateMovieForm
    template_name = "betterboxd/create_movie.html"

    def get_success_url(self):
        """Redirect to main page on success."""
        return reverse("show_all_movies")


class CreateReviewView(CreateView):
    """View to create a new review."""

    model = Review
    form_class = CreateReviewForm
    template_name = "betterboxd/create_review.html"

    def get_context_data(self, **kwargs):
        """Add movie to context."""

        context = super().get_context_data(**kwargs)
        movie = Movie.objects.get(pk=self.kwargs["pk"])
        context["movie"] = movie

        return context

    def form_valid(self, form):
        """Validate the form and associate movie and user."""

        movie = Movie.objects.get(pk=self.kwargs["pk"])
        form.instance.movie = movie
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        """Redirect to movie detail on success."""

        return reverse("movie_detail", kwargs={"pk": self.kwargs["pk"]})


class UpdateReviewView(UpdateView):
    """View to update an existing review."""

    model = Review
    form_class = CreateReviewForm
    template_name = "betterboxd/update_review.html"

    def get_success_url(self):
        """Redirect to movie detail on success."""

        return reverse("movie_detail", kwargs={"pk": self.kwargs["pk"]})


class DeleteReviewView(DeleteView):
    """View to delete an existing review."""

    model = Review
    template_name = "betterboxd/delete_review.html"

    def get_success_url(self):
        return reverse("movie_detail", kwargs={"pk": self.kwargs["pk"]})


def addToWatchlist(request, pk):
    """Add a movie to the user's watchlist."""

    movie = Movie.objects.get(pk=pk)
    Watchlist.objects.get_or_create(user=request.user, movie=movie)

    return redirect("movie_detail", pk=pk)


def removeFromWatchlist(request, pk):
    """Remove a movie from the user's watchlist."""

    movie = Movie.objects.get(pk=pk)
    Watchlist.objects.filter(user=request.user, movie=movie).delete()

    return redirect("movie_detail", pk=pk)


class CreateUserView(CreateView):
    """View to create a new user account"""

    form_class = UserCreationForm
    template_name = "betterboxd/create_user.html"

    def form_valid(self, form):
        """Validate create user form"""

        user = form.save()
        login(self.request, user, backend="django.contrib.auth.backends.ModelBackend")

        return redirect("show_all_movies")


class ShowWatchlistView(ListView):
    """View to show the user's watchlist."""

    model = Movie
    template_name = "betterboxd/show_watchlist.html"
    context_object_name = "watchlist_movies"

    def get_queryset(self):
        """Return the queryset of movies in the user's watchlist."""
        watchlist_movies = []

        if self.request.user.is_authenticated:
            watchlist_movie = Watchlist.objects.filter(user=self.request.user)
            for entry in watchlist_movie:
                watchlist_movies.append(entry.movie)

        return watchlist_movies
