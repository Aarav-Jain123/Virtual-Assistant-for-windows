from django.shortcuts import render, redirect
from . import locationdata
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

name_of_user = None
email_of_user = None
password_of_user = None
token_or_otp = None
check_user = None


def index(request):
    if request.user.is_anonymous:
        return redirect('signup/')
    return render(request, 'homeother/index.html')


def loginn(request):
    return render(request, 'authenticateuser/login.html')


def signup(request):
    if not request.user.is_anonymous:
        return redirect('/')
    return render(request, 'authenticateuser/signup.html')


def indian_news_page(request):
    return render(request, 'homeother/newspage.html', context=locationdata.main)


def send_otp_to_user(request):
    return render(request, 'authenticateuser/otp.html')


def logoutt(request):
    logout(request)
    return redirect('/')


def otp_page(request):
    global name_of_user
    global email_of_user
    global password_of_user
    global check_user

    if not request.user.is_anonymous:
        return redirect('/')
    if request.method == "POST":
        name_of_user = request.POST['fname']
        email_of_user = request.POST['email']
        password_of_user = request.POST['ppassword']
        comfirm_password = request.POST['comfirm-password']
        
        if len(password_of_user) < 8:
            messages.error(request, 'Password should be at least of 8 characters.')
            return redirect('signup/')
        
        if password_of_user != comfirm_password:
            messages.error(request, 'Password and comfirm password fields are not equal.')
            return redirect('signup/')
        
        check_user = authenticate(username=email_of_user, password=password_of_user)
        if check_user is not None:
            login(request, check_user)
            messages.success(request, 'A')
    return render(request, 'authenticateuser/otp.html')