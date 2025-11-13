# File: dadjokes/views.py
# Author: David Myat (amyat@bu.edu), 11/13/2025
# Description: Views for the dadjokes project

import random

from django.shortcuts import render

from .models import *


# Create your views here.
def random(request):
    """Function to respond to "random" joke request that show a random joke and a random picture."""

    model = Joke
    template_name = "dadjokes/random.html"

    random_index = random.randint(0, model.objects.count() - 1)
    random_joke = model.objects.all()[random_index]
    random_picture = Picture.objects.all()[random_index]

    context = {
        "joke": random_joke,
        "picture": random_picture,
    }

    return render(request, template_name, context)


def show_all_jokes(request):
    """Function to respond to "jokes" request."""

    model = Joke
    template_name = "dadjokes/show_all_jokes.html"

    all_jokes = model.objects.all()

    context = {"jokes": all_jokes}

    return render(request, template_name, context)


def index_joke(request):
    """Function to get joke by primary key index."""

    model = Joke
    template_name = "dadjokes/index.html"

    index = request.GET.get("index", 0)
    joke = model.objects.get(pk=index)

    context = {"joke": joke}

    return render(request, template_name, context)


def show_all_pictures(request):
    """Function to respond to "pictures" request."""

    model = Picture
    template_name = "dadjokes/show_all_pictures.html"

    all_pictures = model.objects.all()

    context = {"pictures": all_pictures}

    return render(request, template_name, context)


def index_picture(request):
    """Function to get picture by primary key index."""

    model = Picture
    template_name = "dadjokes/index.html"

    index = request.GET.get("index", 0)
    picture = model.objects.get(pk=index)

    context = {"picture": picture}

    return render(request, template_name, context)
