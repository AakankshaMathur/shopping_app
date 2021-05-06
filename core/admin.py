from django.contrib import admin
from .models import UserProfile, Product, Category, SubCategory, Size, Order, Address, OrderItem
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Size)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)

# class AdressInline(admin.TabularInline):
#     model = Address
