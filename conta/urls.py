from django.urls import path
from django.urls.conf import include
from .views import escolha_tipo_conta, pagina_inicial

app_name = 'conta_bancaria'

urlpatterns = [
    path('escolha_tipo_conta/', escolha_tipo_conta, name='escolha_tipo_conta'),
    path('', pagina_inicial, name='pagina_inicial'),
]