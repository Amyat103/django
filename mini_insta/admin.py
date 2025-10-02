# File: mini_insta/admin.py
# Author: David Myat (amyat@bu.edu), 9/25/2025
# Description: Admin configuration for the mini_insta project
from django.contrib import admin

# Register your models here.
# import Profile and register to admin
from .models import Photo, Post, Profile

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)
