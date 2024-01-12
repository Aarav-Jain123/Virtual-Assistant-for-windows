from django.shortcuts import render, redirect
from . import locationdata, otherfuncs
from django.contrib.auth import logout
from .models import *
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        pin_code = request.POST['pin-code']
        otherfuncs.verify_user(request, city, state, country, pin_code)
    if request.user.is_anonymous: return redirect('signup/')
    if request.user.is_anonymous and UserProfile.is_verified: return redirect('locationform/')
    return render(request, 'homeother/index.html')


def loginn(request):
    if not request.user.is_anonymous:
        return redirect('/')
    
    if request.method == "POST":
        email_of_user = request.POST['email']
        password_of_user = request.POST['ppassword']
        comfirm_password = request.POST['comfirm-password']
        otherfuncs.basic_authentication_conditions(request, email_of_user, password_of_user, comfirm_password)
        return redirect('/otp/')

    return render(request, 'authenticateuser/login.html')


def signup(request):
    if request.method == "POST":
        name_of_user = request.POST['fname']
        email_of_user = request.POST['email']
        password_of_user = request.POST['ppassword']
        comfirm_password = request.POST['comfirm-password']
        otherfuncs.basic_authentication_conditions(request, name_of_user, email_of_user, password_of_user, comfirm_password)
        return redirect('/otp/')

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
    if not request.user.is_anonymous:
        return redirect('/')
    return render(request, 'authenticateuser/otp.html')


def location_form(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        otherfuncs.check_if_in_user_spreadsheet(request, otp)
    if UserProfile.is_verified:
        return redirect('/')
    return render(request, 'authenticateuser/locationform.html')