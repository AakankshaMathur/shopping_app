from django import forms
from .models import UserProfile, Address
from django_countries.fields import CountryField

ADDRESS_TYPE = [
    ('Billing Address', 'Billing Address'),
    ('Shipping Address', 'Shipping Address'),
]

PAYMENT_CHOICES = [
    ('COD' , 'Cash on Delivery'),
    ('Card' , 'Card'),
]

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]

class ProfileForm(forms.ModelForm):

    # name = forms.CharField()
    # contact = forms.CharField()
    # image = forms.ImageField()
    # email = forms.EmailField()
    # address = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":10}))
    # city = forms.CharField()
    # state = forms.CharField()
    # country = CountryField().formfield()

    # address_type = forms.CharField(widget=forms.Select(ADDRESS_TYPE))

    class Meta:
        model = UserProfile
        # fields = "__all__"
        exclude = [ 'address','created_at', 'user']

class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = "__all__"

# class CheckoutForm(forms.Form):
#     name = forms.CharField(required = False)
#     email = forms.CharField(required = False)
#     phone = forms.CharField(required = False)
#     address = forms.CharField(widget = forms.Textarea(attrs={"rows":10, "cols":10}))
#     city = forms.CharField(required = False)
    # country = forms.CountryField(blank = '(select country)')
    # same_billing_address = forms.BooleanField(required = False) 
    # payment_option = forms.ChoiceField(widget = forms.RadioSelect, choices = PAYMENT_CHOICES)

   
class QuantityForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)