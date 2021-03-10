from django import forms
from .models import UserProfile, Address
from django_countries.fields import CountryField

ADDRESS_TYPE = [
    ('Billing Address', 'Billing Address'),
    ('Shipping Address', 'Shipping Address'),
]

class ProfileForm(forms.ModelForm):

    # name = forms.CharField()
    # contact = forms.CharField()
    # image = forms.ImageField()
    # email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":10}))
    city = forms.CharField()
    state = forms.CharField()
    country = CountryField().formfield()

    # address_type = forms.CharField(widget=forms.Select(ADDRESS_TYPE))

    class Meta:
        model = UserProfile
        # fields = "__all__"
        exclude = [ 'address','created_at', 'user']

class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = "__all__"
   
   