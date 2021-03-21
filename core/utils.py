
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import UserProfile
from django.conf import settings

import os


def create_user(request,*args, **kwargs):
    """function to register the user"""
    password = kwargs.pop("password")
    
    username = kwargs.pop("username")
    user = User.objects.create_user(username, username, password)

    user.save()

    profile = UserProfile.objects.create(user=user, name=username, )

    user = authenticate(username=username, password=password)
    login(request, user)
    return profile

