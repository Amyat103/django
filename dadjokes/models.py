# File: dadjokes/models.py
# Author: David Myat (amyat@bu.edu), 10/28/2025
# Description: Define data models for the dadjokes project
from django.db import models
from django.urls import reverse


# Create your models here.
class Joke(models.Model):
    """Store the data for one joke."""

    text = models.TextField()
    name = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of Joke object."""
        return f"{self.name}"


class Picture(models.Model):
    """Store the data for one silly picture/GIF."""

    image_url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)
