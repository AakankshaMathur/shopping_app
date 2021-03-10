from django.urls import path, include
from .views import *


urlpatterns = [
    path('home/signup/', signup_view, name="signup"),
    path('home/login/', login_view, name="login"),
    path('home/logout/', logout_view, name="logout"),
    path('home/', home_view, name="home"),
    path('home/profile/', profile_view, name="profile"),
    path('home/products/', products_view, name="products"),
    path('home/detail/', productdetail_view, name="productdetail"),
    # path('home/product/category', category_view, name="category_view"),
    
]