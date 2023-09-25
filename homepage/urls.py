from django.contrib import admin
from django.urls import path
from .views import homepage, fazer_login

app_name = 'homepage'

urlpatterns = [
    path('', homepage, name='homepage'),
    #path('criar_conta/', criar_conta, name='criar_conta'),
    path('login/', fazer_login, name='login')
]