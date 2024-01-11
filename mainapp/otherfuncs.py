from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from random import randint
from django.contrib.auth.models import User

user = None
token = None

def basic_authentication_conditions(request, name_of_user, email_of_user, password_of_user, comfirm_password):
    global user
    global token

    if len(password_of_user) < 8:
        messages.error(request, 'Password should be at least of 8 characters.')
        return redirect('signup/')
        
    if password_of_user != comfirm_password:
        messages.error(request, 'Password and comfirm password fields are not equal.')
        return redirect('signup/')

    token = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
    send_otp(email_of_user, token)
    verify_user(request, name_of_user, email_of_user, password_of_user, token)


def send_otp(email, token):
    subject = 'Your OTP is here'
    msg = f'Here is your otp: {token}. Hope Indigo helps you!'
    from_email = settings.EMAIL_HOST_USER
    recipients = [email]
    send_mail(subject, msg, from_email, recipients)


def verify_user(request, name, username, password, otp):
    global user

    if token == otp:


        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user=user)
            return redirect('/')
        
        if user is None:
            user = User.objects.create_user(username=username, email=username, password=password, first_name=name)
            user.set_password(password)
            login(request, user)
            return redirect('/')
    else:
        messages.error('Invalid otp.')
        return redirect('/')
