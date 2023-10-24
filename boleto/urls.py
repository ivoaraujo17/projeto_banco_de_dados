from django.urls import path
from django.urls.conf import include
from .views import *

app_name = 'boleto'

urlpatterns = [
    path('depositar/', boletos, name='depositar'),
    path('gerar_boleto/', criar_boleto, name='gerar_boleto'),
    path('pagar_boleto/', pagar_boleto, name='pagar_boleto'),
]