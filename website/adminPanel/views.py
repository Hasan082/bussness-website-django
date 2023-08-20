from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    if request.user.is_authenticated:
        return render(request, 'adminpanel/index.html')
    else:
        return redirect('login')
    
    

def reg_user(request):
    if request.method == 'POST':
        first_name          = request.POST.get('f_name')
        last_name           = request.POST.get('l_name')
        user_name           = request.POST.get('u_name')
        email               = request.POST.get('email')
        password            = request.POST.get('pass_1')
        conf_password       = request.POST.get('pass_2')

        if password != conf_password:
            return redirect('register')
        else:
            user_reg = User.objects.create_user(user_name,email,password)
            user_reg.first_name = first_name
            user_reg.last_name  = last_name
            user_reg.save()
            return redirect('login')

    return render(request, 'adminpanel/register.html')


def login_user(request):
    if request.method == 'POST':
        user_name = request.POST.get('u_name')
        password = request.POST.get('password')

        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('login')

    return render(request, 'adminpanel/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')