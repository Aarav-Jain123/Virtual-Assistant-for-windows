from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from random import randint
from django.contrib.auth.models import User
from .models import *

tokenn = None
name_of_user = None
email_of_user = None
password_of_user = None
comfirm_password = None
user = None


def basic_authentication_conditions(request, *credentialss):
    global tokenn
    global name_of_user
    global email_of_user
    global password_of_user
    global comfirm_password

    try:
        name_of_user, email_of_user, password_of_user, comfirm_password = credentialss
    except Exception:
        email_of_user, password_of_user, comfirm_password = credentialss
    
    try:
        if len(password_of_user) < 8:
            messages.error(request, 'Password should be at least of 8 characters.')
            return redirect('/')
            
        if password_of_user != comfirm_password:
            messages.error(request, 'Password and comfirm password fields are not equal.')
            return redirect('/')
        
    except Exception:
        messages.error(request, 'Please fill the form properly')
        return redirect('/')
    else:
        tokenn = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
        send_otp(email_of_user, tokenn)


def send_otp(email, token):
    subject = 'Your OTP is here'
    msg = f'Here is your otp: {token}. Hope Indigo helps you!'
    from_email = settings.EMAIL_HOST_USER
    recipients = [email]
    send_mail(subject, msg, from_email, recipients)


def check_if_in_user_spreadsheet(request, otp):
    global name_of_user
    global email_of_user
    global password_of_user
    global tokenn
    global user

    if tokenn == otp:
        user = authenticate(username=email_of_user, password=password_of_user)

        if user is not None:
            messages.error(request, "Account already created!")
            return redirect('/')
        
        if user is None:
            user = User.objects.create_user(
username=email_of_user, 
email=email_of_user, 
password=password_of_user, 
first_name=name_of_user
)
            
            user.set_password(password_of_user)
            user.save()
            login(request, user)
            return redirect('/')
    else:
        messages.error('Invalid otp.')
        return redirect('/')


def verify_user(request, city, state, country, pin_code):
    user_profile = UserProfile.objects.create(
name=name_of_user, 
username=email_of_user, 
email=email_of_user, 
password=password_of_user, 
auth_token=tokenn, 
is_verified=True, 
country=country, 
state=state, 
city=city, 
pin_code=pin_code
)
    
    user_profile.save()
    
    login(request, user)

    return redirect('/')