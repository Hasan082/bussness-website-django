from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from adminPanel.models import aboutus
from django.contrib import messages
# from django.http import HttpResponseRedirect
# from django.urls import reverse




def index(request):
    if request.user.is_authenticated:
        return render(request, 'adminpanel/index.html')
    else:
        return redirect('login')
        #return HttpResponseRedirect(reverse('login'))
    
    

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



def about_add(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES.get('about_pic'):
            about_title     = request.POST.get('title')
            about_desc_1    = request.POST.get('desc_1')
            about_desc_2    = request.POST.get('desc_2')
            btn_text        = request.POST.get('btn_text')
            btn_url         = request.POST.get('btn_url')
            about_pic       = request.FILES['about_pic']


            about_save = aboutus(
                about_title     = about_title,
                about_desc_1    = about_desc_1,
                about_desc_2    = about_desc_2,
                btn_text        = btn_text,
                btn_url         = btn_url,
                about_pic       = about_pic
            )

            messages.success(request, 'Data Submitted Successfully')
            about_save.save()
            return redirect('aboutadd')

        return render(request, 'adminpanel/about-add.html')
    else:
        return redirect('login')
    


def about_show(request):
    if request.user.is_authenticated:
        about_data = aboutus.objects.all()
        return render(request, 'adminpanel/aboutshow.html', {'about_data':about_data})
    else:
        return redirect('login')
    

def aboutedit(request, id):
    about_edit = aboutus.objects.filter(id = id)
    return render(request, 'adminpanel/aboutedit.html', {'about_edit': about_edit})


def aboutupdate(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES.get('about_pic'):
            about_title     = request.POST.get('title')
            about_desc_1     = request.POST.get('desc_1')
            about_desc_2     = request.POST.get('desc_2')
            btn_text        = request.POST.get('btn_text')
            btn_url         = request.POST.get('btn_url')
            about_pic       = request.FILES['about_pic']

            about_save = aboutus.objects.filter(id=id)

            about_save = aboutus(
                id=id,
                about_title = about_title,
                about_desc_1 = about_desc_1,
                about_desc_2 = about_desc_2,
                about_readmore_btn_text = btn_text,
                about_readmore_btn_url = btn_url,
                about_pic  = about_pic
            )            
            about_save.save()
            messages.success(request, 'Data Updated Successfully')
            return redirect('aboutshow')

    else:
        return redirect('login')



def about_delete(request, id):
    delete = aboutus.objects.filter(id=id).delete()
    # messages.error(request, "Task Deleted successfully")
    return redirect('aboutshow')