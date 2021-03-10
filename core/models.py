from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField


# Create your models here.

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_profile")
    name = models.CharField(null=True, blank=True, max_length=250)
    contact = models.CharField(null=True, blank=True, max_length=20, unique=True)
    image = models.ImageField(upload_to ='uploads/')
    email = models.EmailField(max_length=254)
    address = models.ManyToManyField('Address')
    created_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Address(models.Model):
    ADDRESS_TYPE = (
        ('Billing Address', 'Billing Address'),
        ('Shipping Address', 'Shipping Address'),
    )

    address = models.TextField(max_length=600, null=True, blank=True)
    city = models.CharField(null=True, blank=True, max_length=20)
    country = CountryField(null=True, blank=True)
    state = models.CharField(null=True, blank=True, max_length=20)
    address_type = models.CharField(choices = ADDRESS_TYPE, max_length=20, null=True, blank=True)



class Product(models.Model):
    product_name = models.CharField(null=True, blank=True, max_length=250)
    product_size = models.ManyToManyField('Size')
    desc = models.TextField(max_length=300, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', related_name='category_type', on_delete=models.CASCADE, null=True, blank=True)
    sub_category = models.ForeignKey('SubCategory', related_name='subcategory_type', on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name="created_by")
    def __str__(self):
        return self.product_name

class Category(models.Model):
    # CATEGORY_TYPE = (
    #     ('Men', 'Men'),
    #     ('Women', 'Women'),
    # )

    # SUBCATEGORY_TYPE = (
    #     ('Indian', 'Indian'),
    #     ('Western', 'Western'),
    #     ('Accessories', 'Accessories'),
    # )

    category_name = models.CharField(max_length=50, null=True, blank=True)
    # subcategory_name = models.CharField(choices=SUBCATEGORY_TYPE, max_length=50, null=True, blank=True)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=50, null=True, blank=True)
   
    def __str__(self):
        return self.subcategory_name

class Size(models.Model):
    size = models.CharField(max_length=50, null=True, blank=True)

    def  __str__(self):
        return self.size

class Order(models.Model):
    customer = models.ForeignKey('UserProfile', related_name='customername', on_delete=models.DO_NOTHING, null=True, blank=True)
    customer_address = models.ForeignKey('Address', related_name='customeraddress', on_delete=models.DO_NOTHING, null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)
    product_quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(null=True, blank=True)