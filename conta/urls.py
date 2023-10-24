from django.urls import path
from django.urls.conf import include
from .views import *

app_name = 'conta_bancaria'

urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('escolha_tipo_conta/', escolha_tipo_conta, name='escolha_tipo_conta'),
    path('criar_conta_corrente/', criar_conta_corrente, name='criar_conta_corrente'),
    path('criar_conta_poupanca/', criar_conta_poupanca, name='criar_conta_poupanca'),
    path('criar_conta_salario/', criar_conta_salario, name='criar_conta_salario'),
    path('minha_conta/<int:numero_conta>', minha_conta, name='minha_conta'),
    path('minha_conta/<int:numero_conta>/boletos/',  include('boleto.urls')),
]