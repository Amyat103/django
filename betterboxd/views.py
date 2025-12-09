from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from .forms import CreateMovieForm, CreateReviewForm
from .models import Movie, Review


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


class ShowMovieDetail(DetailView):
    """Function to respond to movie detail request."""

    model = Movie
    template_name = "betterboxd/movie_detail.html"
    context_object_name = "movie"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = self.object.reviews.all()
        return context


class CreateMovieView(CreateView):
    """View to create a new movie."""

    model = Movie
    form_class = CreateMovieForm
    template_name = "betterboxd/create_movie.html"

    def get_success_url(self):
        return reverse("show_all_movies")


class CreateReviewView(CreateView):
    """View to create a new review."""

    model = Review
    form_class = CreateReviewForm
    template_name = "betterboxd/create_review.html"

    def form_valid(self, form):
        form.instance.movie_id = self.kwargs["pk"]
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("movie_detail", kwargs={"pk": self.kwargs["pk"]})


class UpdateReviewView(CreateView):
    """View to update an existing review."""

    model = Review
    form_class = CreateReviewForm
    template_name = "betterboxd/update_review.html"

    def get_success_url(self):
        return reverse("movie_detail", kwargs={"pk": self.kwargs["pk"]})


class DeleteReviewView(CreateView):
    """View to delete an existing review."""

    model = Review
    template_name = "betterboxd/delete_review.html"

    def get_success_url(self):
        return reverse("movie_detail", kwargs={"pk": self.kwargs["pk"]})


def addToWatchlist(request, movie_id):
    """Add a movie to the user's watchlist."""
    movie = Movie.objects.get(id=movie_id)
    request.user.profile.watchlist.add(movie)

    return redirect("movie_detail", pk=movie_id)


def removeFromWatchlist(request, movie_id):
    """Remove a movie from the user's watchlist."""
    movie = Movie.objects.get(id=movie_id)
    request.user.profile.watchlist.remove(movie)

    return redirect("movie_detail", pk=movie_id)
