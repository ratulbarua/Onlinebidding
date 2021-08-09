from django import forms
from .models import about
from django.forms import ModelForm



class ContactUs(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = '__all__'
