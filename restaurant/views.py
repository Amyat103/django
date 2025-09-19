import random
from datetime import datetime, timedelta

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

    template_name = "restaurant/confirmation.html"

    # map to original name with spaces
    names = {
        "shrimp": "Shrimp",
        "king_crab": "King Crab",
        "clams": "Clams",
        "dungeness_crab": "Dungeness Crab",
        "snow_crab": "Snow Crab",
    }

    # map prices to seafood for calc
    prices = {
        "shrimp": 16,
        "king_crab": 95,
        "clams": 19,
        "dungeness_crab": 35,
        "snow_crab": 45,
    }

    # to map sauce names for confirmation page
    sauces_names = {
        "the_whole_shabang": "The Whole Shabang",
        "cajun": "Cajun",
        "lemon_pepper": "Lemon Pepper",
    }

    if request.POST:
        seafood = request.POST.getlist("seafood")
        daily_special = request.POST["daily_special"]
        sauce = sauces_names[request.POST["sauce"]]
        spice_level = request.POST["spice_level"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        special_requests = request.POST.get("special_requests")

    # calculate total price and add 50 if daily special exists
    total_price = 0
    for order in seafood:
        total_price += prices[order]

    if daily_special:
        total_price += 50

    # map and add to list with formatted names
    seafood_orders = []
    for order in seafood:
        format_name = names[order]
        seafood_orders.append(format_name)

    # calculate ready time with random
    curr_time = datetime.now()
    random_min = random.randint(30, 60)
    ready_time = curr_time + timedelta(minutes=random_min)

    context = {
        "seafood": seafood_orders,
        "daily_special": daily_special,
        "sauce": sauce,
        "spice_level": spice_level,
        "name": name,
        "email": email,
        "phone": phone,
        "total_price": total_price,
        "ready_time": ready_time,
        "special_requests": special_requests,
    }

    return render(request, template_name, context)


# def confirmation(request):
#     """Function to respond to "confirmation" request."""

#     template_name = "restaurant/confirmation.html"
#     return render(request, template_name)
