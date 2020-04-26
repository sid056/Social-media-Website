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


class NewUerForm(UserCreationForm) :

    class Meta :
        model = User
        fields = (
            'username' ,
            'first_name',
            'last_name' ,
            'email',
            'password1' ,
            'password2' ,
        )
    def save(self , commit=True):
        user = super(NewUerForm, self ).save(commit=False)
        user.first_name = self.cleaned_data['first_name'],
        user.last_name = self.cleaned_data['last_name'],        
        user.email = self.cleaned_data['email'],

        print(user)

        if commit :
            user.save()
        return user
    

