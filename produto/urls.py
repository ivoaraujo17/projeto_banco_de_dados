from django.urls import path
from django.urls.conf import include
from concessao.views import *
from .views import *

app_name = 'produto'

urlpatterns = [
    path('<int:numero_conta>/emprestimo/', emprestimo, name='emprestimo'),
    path('<int:numero_conta>/financiamento/', financiamento, name='financiamento'),
    path('<int:numero_conta>/consorcio/', consorcio, name='consorcio'),
    path('<int:numero_conta>/emprestimos_conta/', emprestimos_conta, name='emprestimos_conta'),
]