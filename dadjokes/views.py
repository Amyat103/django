# File: dadjokes/views.py
# Author: David Myat (amyat@bu.edu), 11/13/2025
# Description: Views for the dadjokes project

import random

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render

from .models import *
from .models import Joke, Picture
from .serializers import JokeSerializer, PictureSerializer


# Create your views here.
def show_random(request):
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
    template_name = "dadjokes/all_jokes.html"

    all_jokes = model.objects.all()

    context = {"jokes": all_jokes}

    return render(request, template_name, context)


def index_joke(request, index):
    """Function to get joke by primary key index."""

    model = Joke
    template_name = "dadjokes/index.html"

    joke = model.objects.get(pk=index)

    context = {"joke": joke}

    return render(request, template_name, context)


def show_all_pictures(request):
    """Function to respond to "pictures" request."""

    model = Picture
    template_name = "dadjokes/all_pictures.html"

    all_pictures = model.objects.all()

    context = {"pictures": all_pictures}

    return render(request, template_name, context)


def index_picture(request, index):
    """Function to get picture by primary key index."""

    model = Picture
    template_name = "dadjokes/index.html"

    picture = model.objects.get(pk=index)

    context = {"picture": picture}

    return render(request, template_name, context)


class JokeListAPIView(generics.ListCreateAPIView):
    """API view to list all jokes or create a new joke."""

    queryset = Joke.objects.all()
    serializer_class = JokeSerializer


class JokeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update, or delete a joke by ID."""

    queryset = Joke.objects.all()
    serializer_class = JokeSerializer


class PictureListAPIView(generics.ListCreateAPIView):
    """API view to list all pictures or create a new picture."""

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class PictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update, or delete a picture by ID."""

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


@api_view(["GET"])
def api_random_joke(request):
    """API view to get a random joke."""

    jokes = Joke.objects.all()
    random_index = random.randint(0, jokes.count() - 1)
    random_joke = jokes[random_index]
    serializer = JokeSerializer(random_joke)
    return Response(serializer.data)


@api_view(["GET"])
def api_random_picture(request):
    """API view to get a random picture."""

    pictures = Picture.objects.all()
    random_index = random.randint(0, pictures.count() - 1)
    random_picture = pictures[random_index]
    serializer = PictureSerializer(random_picture)
    return Response(serializer.data)
