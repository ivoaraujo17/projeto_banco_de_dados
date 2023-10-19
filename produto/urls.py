from django.urls import path
from django.urls.conf import include
from concessao.views import *
from .views import *

app_name = 'produto'

urlpatterns = [
    path('emprestimo/<int:numero_conta>/', emprestimo, name='emprestimo'),
    path('financiamento/<int:numero_conta>/', financiamento, name='financiamento'),
    path('consorcio/<int:numero_conta>/', consorcio, name='consorcio'),
    path('emprestimos_conta/<int:numero_conta>/', emprestimos_conta, name='emprestimos_conta'),
]