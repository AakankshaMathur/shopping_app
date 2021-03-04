
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import UserProfile
from django.conf import settings

import os

def email_validation(email):
    pattern = re.compile(
        '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')
    if pattern.match(email):
        return True
    return None

def create_user(request,*args, **kwargs):
    """function to register the user"""
    password = kwargs.pop("password")
    
    username = kwargs.pop("username")
    user = User.objects.create_user(username,password)

    user.save()

    profile = UserProfile.objects.create(user=user, name=username, )

    user = authenticate(username=username, password=password)
    login(request, user)
    return profile

