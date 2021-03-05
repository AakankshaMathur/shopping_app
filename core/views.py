from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .utils import *
from .models import Product, Category, UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.views import LoginView
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

# def category_view(request, kwargs):
#     category = None
#     slug = None

#     try:
#         slug = kwargs.get('slug')
#     except Exception as e:
#         print(e)
#         pass
#     if slug:
#         category = Category.objects.filter(slug=slug).first()
#     else :
#         category = Category.objects.filter(parent=None).first()

#     return render(request, "product.html", context)


