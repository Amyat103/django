import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

daily_special = [
    "Boston Tea Party King Crab Special",
    "New England Catfish Bundle Special",
    "Shrimp Saturday",
    "Snow Crab Sunday",
]


def main(request):
    """Function to respond to "main" request."""

    # context dict to send in main/ view
    context = {
        "restaurant_img": "https://s3-media0.fl.yelpcdn.com/bphoto/dZOM29XVseq8aSfQgj5c6A/o.jpg",
    }

    template_name = "restaurant/main.html"
    return render(request, template_name, context)


def order(request):
    """Function to respond to "order" form request."""

    # generate random int to index daily special
    random_special_index = random.randint(0, len(daily_special) - 1)

    # context dict to send in daily special to randomize
    context = {
        "daily_special": daily_special[random_special_index],
    }

    template_name = "restaurant/order.html"
    return render(request, template_name, context)


def submit(request):
    """Process the order submission, and generate a result."""

    print(request)
    return HttpResponse("")


def confirmation(request):
    """Function to respond to "confirmation" request."""

    template_name = "restaurant/confirmation.html"
    return render(request, template_name)
