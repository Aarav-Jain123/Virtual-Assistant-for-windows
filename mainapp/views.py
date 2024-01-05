from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'homeother/index.html')

def loginn(request):
    return render(request, 'authenticateuser/login.html')


def signup(request):
    return render(request, 'authenticateuser/signup.html')