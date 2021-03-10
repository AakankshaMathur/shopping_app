from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .utils import *
from django.views import generic
from django.urls import reverse_lazy
from .models import Product, Category, UserProfile, Address
from django_countries import countries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth

from .forms import ProfileForm
from django.http import HttpResponse
# from .utils import get_context

from django.contrib.auth import get_user_model


def signup_view(request):
    print("hello")
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)

        valid = True
        print(1)
        if valid is True:
            user = create_user(request, password=password, username=username)
            print(2)
            user.save()
            print(3)
            return redirect('login')

    return render(request, "account.html", context)

    


def login_view(request):
    print("login hello")
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        # valid = True
        # if valid is True:       
        user = authenticate(request, username=username, password=password)
        print(user)
        
        if user is not None:
            login(request, user)
            context['success'] = "Succesfully logged In!!"
            print("l2")
            return redirect('home')

        else:
            print("l3")
            context['error'] = "Invalid Login"
            # return redirect('login')

        #     return redirect('home')
        # else:
        #     return redirect('login')

        # if user is not None:
        #     login(request, user)
        #     return redirect('home')

    return render(request, "account.html", context)

def logout_view(request):
    auth.logout(request)
    return redirect('home')
    # context = {}
    # if request.user.is_authenticated:
    #     return render(request,"index.html", context)
    # else:
    #     return render(request, "index.html", context)
    # return render(request,"index.html", context)

def home_view(request):
    
    context = {}

    return render(request, "index.html", context)

def products_view(request):
    # model = Product
    context = {}

    return render(request, "product.html", context)

def productdetail_view(request):
    model = Product
    context = {}

    return render(request, "product-detail.html", context)

def profile_view(request):
    model = UserProfile
    form = ProfileForm(instance = request.user.user_profile)
    # form = ProfileForm()
    print(form)
    # form = ProfileForm(request.GET)
    context = {'form' : form}
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance= request.user.user_profile)
        print(form.errors)
        print(form, "qwertyyyyyyyyyyyyyyy")
        
        if form.is_valid():
            # obj = Address()
            # obj.address = form.cleaned_data('address')
            # obj.city = form.cleaned_data('city')
            # obj.state = form.cleaned_data('state')
            # obj.country = form.cleaned_data('country')
            # print("valid")
            
            print("valid")
            form.save()
            return redirect('home')
    
    return render(request, "profile.html", context)

    

    # obj.address = form.POST.get('address')
    #         obj.city = form.POST.get('city')
    #         obj.state = form.POST.get('state')
    #         obj.country = form.POST.get('country')