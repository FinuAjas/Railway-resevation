from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from base.views import *
from django.contrib.auth.decorators import login_required


def userlogin(request):
    if request.user.is_authenticated:
        return redirect('home')   
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    else:
        return render(request,'login.html')   

def register(request):
    if request.user.is_authenticated:
        return redirect('home')   

    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.error(request,'Username or Email already taken!')
                return render(request,'register.html') 
            else:    
                user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password1)
                login(request,user)
                return redirect('home')    
        else:
            messages.error(request,'Password does not match!')
            return render(request,'register.html') 
    else:
        return render(request,'register.html') 

@login_required(login_url='userlogin')
def userlogout(request):
    logout(request)
    return redirect('home')
