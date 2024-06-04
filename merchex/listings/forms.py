from django import forms
from .models import Band, Listing


class ContactUsForm(forms.Form):
    
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)
   
   
class BandForm(forms.ModelForm):
    
    class Meta:
        model = Band
        # fields = '__all__'
        exclude = ('active', 'official_homepage')  # if  null=True &/or default=T/F


class ListingForm(forms.ModelForm):
    
    class Meta:
        model = Listing
        # fields = '__all__'
        exclude = ('sold', 'year')  # if  null=True &/or default=T/F
