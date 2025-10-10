# File: mini_insta/forms.py
# Author: David Myat (amyat@bu.edu), 9/30/2025
# Description: Define forms for the mini_insta project
from django import forms

from .models import *


class CreatePostForm(forms.ModelForm):
    """A form to add a post to the database."""

    class Meta:
        """Associate this form with a model from our database."""

        model = Post
        fields = ["caption"]


class UpdatePostForm(forms.ModelForm):
    """A form to update a post in the database."""

    class Meta:
        """Associate this form with a model from our database."""

        model = Post
        fields = ["caption"]
