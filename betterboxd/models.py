# File: betterboxd/models.py
# Author: David Myat (amyat@bu.edu), 12/9/2025
# Description: Models for movies, reviews, and watchlists in BetterBoxd app

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Movie(models.Model):
    """Stores the data for one movie."""

    title = models.TextField()
    year = models.TextField()
    director = models.TextField()
    genre = models.TextField()
    runtime = models.IntegerField()
    description = models.TextField()
    poster = models.TextField()

    def __str__(self):
        """Return string representation of Movie object."""
        return f"{self.title} ({self.year})"


class Review(models.Model):
    """Stores the data for one review."""

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of Review object."""
        return f"Review of {self.movie.title} by {self.user.username} - Rating: {self.rating}"


class Watchlist(models.Model):
    """Stores the data for a user's watchlist."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of Watchlist object."""
        return f"Watchlist of {self.user.username}"
