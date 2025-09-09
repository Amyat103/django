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
