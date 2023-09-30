from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import criar_usuario


app_name = 'cliente'

urlpatterns = [
    path('criar_conta/', criar_usuario, name='criar_conta'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='homepage.html'), name='logout'),
    
]