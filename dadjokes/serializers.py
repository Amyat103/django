# File: dadjokes/serializers.py
# Author: David Myat (amyat@bu.edu), 11/13/2025
# Description: Serializers for the dadjokes REST API

from rest_framework import serializers

from .models import *


class JokeSerializer(serializers.ModelSerializer):
    """Serializer for Joke model."""

    class Meta:
        model = Joke
        fields = ["id", "text", "name", "timestamp"]


class PictureSerializer(serializers.ModelSerializer):
    """Serializer for Picture model."""

    class Meta:
        model = Picture
        fields = ["id", "name", "image_url", "timestamp"]
