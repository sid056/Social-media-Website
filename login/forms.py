from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.Form) :

    username = forms.CharField(widget=forms.TextInput(
        attrs={"class":"form-control",
        "placeholder":"Enter your user_id"}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class":"form-control",
        "placeholder":"Enter your password  "}
    ))
