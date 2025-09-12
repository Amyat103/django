# File: quotes/views.py
# Author: David Myat (amyat@bu.edu), 9/9/2025
# Description: Views for quotes project

import random

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Global variables for views.py
quotes = [
    "If one cannot enjoy reading a book over and over again, there is no use in reading it at all.",
    "We are all in the gutter, but some of us are looking at the stars.",
    "To live is the rarest thing in the world. Most people exist, that is all.",
]
images = [
    "https://images.gr-assets.com/photos/1375466820p8/817846.jpg",
    "https://images.gr-assets.com/authors/1673611182p8/3565.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/9/9c/Oscar_Wilde_portrait.jpg",
]


# Create your views here.
# def home(request):
#     """Function to respond to "home" request."""

#     # var to store the html path of the home page
#     template_name = "quotes/home.html"
#     return render(request, template_name)


def quote(request):
    """Function to respond to "quotes" request."""

    # randomly generate between 0 to length of quotes/images array
    random_quote_index = random.randint(0, len(quotes) - 1)
    random_image_index = random.randint(0, len(images) - 1)

    # context dict to send in random quote into quote/ view
    context = {
        # randomly selected quote/image for the quote page
        "random_quote": quotes[random_quote_index],
        "random_image": images[random_image_index],
    }

    # var to store the html path of the quotes page
    template_name = "quotes/quote.html"
    return render(request, template_name, context)


def show_all(request):
    """Function to respond to "show_all" request."""

    # context dict to send all quotes/images to show_all view
    context = {
        "quotes": quotes,
        "images": images,
    }

    # var to store the html path of the show_all page
    template_name = "quotes/show_all.html"
    return render(request, template_name, context)


def about(request):
    """Function to respond to "about" request."""

    # context dict to send image of author to about/ view
    context = {
        "author_image": images[0],
    }

    # var to store the html path of the about page
    template_name = "quotes/about.html"
    return render(request, template_name, context)
