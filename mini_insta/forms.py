# File: mini_insta/models.py
# Author: David Myat (amyat@bu.edu), 9/25/2025
# Description: Define data models for the mini_insta project
from django import forms

from .models import Profile


class CreatePostForm(forms.ModelForm):
    """A form to add a post to the database."""

    class Meta:
        """Associate this form with a model from our database."""

        model = Profile
