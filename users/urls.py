from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('',views.userlogin,name='userlogin'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('register',views.register,name='register')
]