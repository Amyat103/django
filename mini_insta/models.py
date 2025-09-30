# File: mini_insta/models.py
# Author: David Myat (amyat@bu.edu), 9/25/2025
# Description: Define data models for the mini_insta project
from django.db import models


# Create your models here.
class Profile(models.Model):
    """Encapsulate data of a profile of a user"""

    # define data attribute of the Profile model
    username = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    # auto set join date to current time
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return string representation of Profile object"""
        return f"{self.username} | {self.display_name}"


class Post(models.Model):
    """Encapsulate data of a post made by a user"""

    # define data attributes of the Post model
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        """return string representation of Post object"""
        return f"Posted by {self.profile.username} | {self.timestamp}"


class Photo(models.Model):
    """Encapsulate data of a photo in a post"""

    # define data attributes of the Photo model
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return string representation of Photo object"""
        return f"Photo posted by {self.post.profile.username} | {self.timestamp}"
