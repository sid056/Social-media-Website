from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required()
def HomeView(request):
    if request.user.is_authenticated :
        return render(request,'home.html',{'user':request.user.username})
    else :
        return render(request,'login.html')

@login_required()
def ProfileView(request,username) :
    user = User.objects.get(username=username)
    if request.user.is_authenticated :
        if request.user == user :
            return render(request, 'own_profile.html' , {'user':user})
        else :
            return render(request, 'other_profile.html' , {'user':user})

def CreateUser(request):
    print(hi)

