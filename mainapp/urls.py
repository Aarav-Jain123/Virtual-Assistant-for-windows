from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='Signup'),
    path('login/', loginn, name='Login'),
    # path('newspage/', indian_news_page, name='News'),
    path('otp/', send_otp_to_user, name="OTP"),
]
