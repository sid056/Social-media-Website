from django.shortcuts import render,redirect
from .forms import UserForm,NewUerForm
from django.contrib.auth import authenticate,login,logout

def Login(request) :
    if request.method == 'GET' :

        form = UserForm()
        return render(request , 'login.html' , {'form':form})

    if request.method == 'POST' :
        

        form = UserForm(request.POST)
        
        if form.is_valid() :
             username = form.cleaned_data['username']
             password = form.cleaned_data['password']
             user = authenticate(request , username=username , password=password)
             if user is not None : 
                 login(request,user)
                 return redirect('home')
             else :

                print("user fucked up ")
                form = UserForm()
                return render(request , 'login.html' , {'form':form})


def SignupView(request) :
    if request.method == 'POST' :
        form = NewUerForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/')
        else :                
                print("FORM  OOMBI")

    else :

        form = NewUerForm()


    return render(request,'signup.html',{'form':form})    

def LogoutView(request) :

    logout(request)
    return redirect('/')

