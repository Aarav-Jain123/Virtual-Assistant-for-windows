from django.shortcuts import render, redirect
from . import locationdata, otherfuncs
from django.contrib.auth import logout
from .models import *

# Basic Authentication
name_of_user = None
email_of_user = None
password_of_user = None
token = None
check_user = None

# After authentication
pin_code = None
city = None
state = None
country = None


def index(request):
    if request.user.is_anonymous:
        return redirect('signup/')
    if request.method == 'POST':
        otp = request.POST['otp']
        otherfuncs.verify_user(request=request, name=name_of_user, username=email_of_user, password=password_of_user, otp=otp)
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
    global token

    if not request.user.is_anonymous:
        return redirect('/')
    if request.method == "POST":
        name_of_user = request.POST['fname']
        email_of_user = request.POST['email']
        password_of_user = request.POST['ppassword']
        comfirm_password = request.POST['comfirm-password']

        otherfuncs.basic_authentication_conditions(request, name_of_user, email_of_user, password_of_user, comfirm_password)
    return render(request, 'authenticateuser/otp.html')


def other_details(request):
    return render(request, 'authenticateuser/otherdetails.html')