# File: quotes/views.py
# Author: David Myat (amyat@bu.edu), 9/9/2025
# Description: Views for quotes project

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    """Function to respond to "home" request."""

    # var to store the html path of the home page
    template_name = "quotes/home.html"
    return render(request, template_name)


def quotes(request):
    """Function to respond to "quotes" request."""

    # var to store the html path of the quotes page
    template_name = "quotes/quotes.html"
    return render(request, template_name)


def show_all(request):
    """Function to respond to "show_all" request."""

    # var to store the html path of the show_all page
    template_name = "quotes/show_all.html"
    return render(request, template_name)


def about(request):
    """Function to respond to "about" request."""

    # var to store the html path of the about page
    template_name = "quotes/about.html"
    return render(request, template_name)
