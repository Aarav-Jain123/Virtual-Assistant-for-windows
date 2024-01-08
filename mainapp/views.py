from django.shortcuts import render
from . import extractnews


# Create your views here.
def index(request):
    return render(request, 'homeother/index.html')


def loginn(request):
    return render(request, 'authenticateuser/login.html')


def signup(request):
    return render(request, 'authenticateuser/signup.html')


def indian_news_page(request):
    return render(request, 'homeother/newspage.html', context=extractnews.main)


def send_otp_to_user(request):
    return render(request, 'authenticateuser/otp.html')