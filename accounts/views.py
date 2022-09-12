from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Registration form -----------------------------------------------
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username=data['user_name'], email=data['email'],
                                     first_name=data['first_name'], last_name=data['last_name'],
                                     password=data['password_2'])
            messages.success(request, 'ثبت نام با موفقیت انجام شد',extra_tags='success ')
            return redirect('home:home')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


# login form -------------------------------------------------------
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = authenticate(request, username=User.objects.get(email=data['user']), password=data['password'])
            except:
                user = authenticate(request, username=data['user'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'به فروشگاه جنگو خوش آمدید', extra_tags='secondary')
                return redirect('home:home')
            else:
                messages.error(request, 'نام کاربری و یا رمز عبور شما اشتباه است', extra_tags='danger')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# logout form -------------------------------------------------------
def user_logout(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید', extra_tags='success')
    return redirect('home:home')


# profile form -------------------------------------------------------
def user_profile(request):
    return render(request, 'accounts/profile.html')
















