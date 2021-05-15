from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from django.db.models import Sum


# Create your models here.

User = get_user_model()

ADDRESS_TYPE = (
        ('Billing Address', 'Billing Address'),
        ('Shipping Address', 'Shipping Address'),
    )

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
   
    # username = models.ManyToManyField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_address")
    address = models.TextField(max_length=600, null=True, blank=True)
    city = models.CharField(null=True, blank=True, max_length=20)
    country = CountryField(null=True, blank=True)
    state = models.CharField(null=True, blank=True, max_length=20)
    address_type = models.CharField(choices = ADDRESS_TYPE, max_length=20, null=True, blank=True)



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(null=True, blank=True, max_length=250)
    image = models.ImageField(upload_to ='media/', null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True,blank=True)
    product_size = models.ManyToManyField('Size')
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    desc = models.TextField(max_length=300, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', related_name='category_type', on_delete=models.CASCADE, null=True, blank=True)
    sub_category = models.ForeignKey('SubCategory', related_name='subcategory_type', on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name="created_by")
    
    def get_absolute_url(self):
        return f"home/detail/{self.slug}/"
    def __str__(self):
        return self.product_name

    def admin_image(self):
        return '<img src="%s"/>' % self.image
    admin_image.allow_tags = True

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
    slug = models.SlugField(max_length=255, unique=True, null=True,blank=True)
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
    # slug = models.SlugField(max_length=255, unique=True, null=True,blank=True)
    customer = models.ForeignKey('UserProfile', related_name='customername', on_delete=models.DO_NOTHING, null=True, blank=True)
    customer_address = models.ForeignKey('Address', related_name='customeraddress', on_delete=models.DO_NOTHING, null=True, blank=True)
    product_name = models.ForeignKey('Product',related_name='productname', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(null=True, blank=True)
    shipping_address = models.ForeignKey(Address, related_name="shipping_address", on_delete=models.SET_NULL, blank = True, null = True)
    billing_address = models.ForeignKey(Address, related_name="billing_address", on_delete=models.SET_NULL, blank = True, null = True)
    date_ordered = models.DateTimeField(auto_now_add = True, blank = True, null = True)

    # def __str__(self):
    #     return self.customer.name

    def get_absolute_url(self):
        return f"home/cart/{self.slug}/"

    # def __unicode__(self):
    #     "Order id: %s" %(self.id)

    # @property
    # def get_cart_total(self):
    #     orderitems = self.orderitem_set.all()
    #     total = Sum([item.get_total for item in items])
    #     return total

    # @property
    # def get_cart_items(self):
    #     orderitems = self.orderitem_set.all()
    #     total = Sum([item.quantity for item in orderitems])
    #     return total
    
    @property    
    def get_total(self):
        total = 0
        try:
            total = self.quantity * self.price
            
        except:
            pass

        return total
    
   

# OrderItem table not needed until we go for multiple products checkout
class OrderItem(models.Model):
    product_name = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    quantity = models.IntegerField(default = 1, null = True,blank = True)

    # property decorator is used so that we can access the function in our template also
    @property    
    def get_total(self):
        total = self.product.total_price * self.product.price
        return total
    
