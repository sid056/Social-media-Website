from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post,Following_list

@login_required()
def HomeView(request):
    following=[]
    posts = Post.objects.all().order_by('-id')
    Following = Following_list.following_list(Following_list,request.user)
    for follows in Following :
        following.append(follows.following)
    print(following)
    if request.user.is_authenticated :
        return render(request,'home.html',{'user':request.user.username , 'posts':posts , 'following':following })
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

