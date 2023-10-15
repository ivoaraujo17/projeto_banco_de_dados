from django.urls import path
from django.urls.conf import include
from .views import *

app_name = 'concessao'

urlpatterns = [
    path('concessao/', solicitar_concessao, name='concessao'),
]