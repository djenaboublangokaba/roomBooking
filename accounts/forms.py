from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from locationblango.models import Booking

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))




    class Meta:
        model = User
        fields=['username', 'email', 'password1', 'password2','is_customer', 'is_employee']



class BookingForm(forms.ModelForm):
    check_in = forms.DateField(required=True, input_formats= ['%Y-%m-%d',])
    check_out  = forms.DateField(required=True, input_formats= ['%Y-%m-%d',])


    class Meta:
        model = Booking
        fields = ['room','check_in','check_out']