from django import forms

from .models import Movie, Review


class CreateMovieForm(forms.ModelForm):
    """Form to add a movie to the database."""

    class Meta:
        """Associate this form with a model from our database."""

        model = Movie
        fields = [
            "title",
            "year",
            "genre",
            "director",
            "runtime",
            "description",
            "poster",
        ]


class CreateReviewForm(forms.ModelForm):
    """Form to add a review to the database."""

    class Meta:
        """Associate this form with a model from our database."""

        model = Review
        fields = ["movie", "review_text", "rating"]


class UpdateReviewForm(forms.ModelForm):
    """Form to update a review in the database."""

    class Meta:
        """Associate this form with a model from our database."""

        model = Review
        fields = ["review_text", "rating"]


class UpdateMovieForm(forms.ModelForm):
    """Form to update a movie in the database."""

    class Meta:
        """Associate this form with a model from our database."""

        model = Movie
        fields = [
            "title",
            "year",
            "genre",
            "director",
            "runtime",
            "description",
            "poster",
        ]
