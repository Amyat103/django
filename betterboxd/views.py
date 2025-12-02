from django.shortcuts import render


# Create your views here.
def home(request):
    """Function to respond to home request."""

    template_name = "betterboxd/home.html"
    return render(request, template_name)


def profile(request):
    """Function to respond to profile request."""

    template_name = "betterboxd/profile.html"
    return render(request, template_name)


def movie_detail(request, movie_id):
    """Function to respond to movie detail request."""

    context = {
        "movie_id": movie_id,
    }

    template_name = "betterboxd/movie_detail.html"
    return render(request, template_name, context)


def login(request):
    """Function to respond to login request."""

    template_name = "betterboxd/login.html"
    return render(request, template_name)
