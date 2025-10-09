# File: mini_insta/models.py
# Author: David Myat (amyat@bu.edu), 9/25/2025
# Description: Define data models for the mini_insta project
from django.db import models
from django.urls import reverse


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

    def get_all_posts(self):
        """Return QuerySet of all posts for this profile."""
        posts = Post.objects.filter(profile=self).order_by("timestamp")
        return posts


class Post(models.Model):
    """Encapsulate data of a post made by a user"""

    # define data attributes of the Post model
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        """return string representation of Post object"""
        return f"Posted by {self.profile.username} | {self.caption} | {self.timestamp}"

    def get_absolute_url(self):
        """Return a url to display one instance of Post"""
        return reverse("post", kwargs={"pk": self.pk})

    def get_all_photos(self):
        """Return QuerySet of all photos for this post."""
        photos = Photo.objects.filter(post=self).order_by("timestamp")
        return photos

    def get_first_photo(self):
        """Return first photo for a post or default image if none exists."""
        first_photo = Photo.objects.filter(post=self).order_by("timestamp").first()
        # return first photo or default image
        if first_photo:
            return first_photo.image_url
        else:
            return "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/1665px-No-Image-Placeholder.svg.png"


class Photo(models.Model):
    """Encapsulate data of a photo in a post"""

    # define data attributes of the Photo model
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(blank=True)

    def __str__(self):
        """return string representation of Photo object"""
        return f"Photo posted by {self.post.profile.username}| tied to post: {self.post} | {self.timestamp}"
