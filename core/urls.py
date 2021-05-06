from django.urls import path, include
from .views import *


urlpatterns = [
    path('home/signup/', signup_view, name="signup"),
    path('home/login/', login_view, name="login"),
    path('home/logout/', logout_view, name="logout"),
    path('home/', home_view, name="home"),
    path('home/profile/', profile_view, name="profile"),
    path('home/products/', products_view, name="products"),
    path('home/detail/<slug:slug>/', productdetail_view, name="productdetail"),
    path('home/checkout/', checkout_view, name="checkout"),
    path('home/cart/<slug:slug>/', cart_view, name="cart"),
    # path('home/product/category', category_view, name="category_view"),
    
]