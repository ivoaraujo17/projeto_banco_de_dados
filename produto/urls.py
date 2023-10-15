from django.urls import path
from django.urls.conf import include
from .views import *

app_name = 'produto'

urlpatterns = [
    path('emprestimo/', emprestimo, name='emprestimo'),
    path('financiamento/', financiamento, name='financiamento'),
    path('consorcio/', consorcio, name='consorcio'),
]