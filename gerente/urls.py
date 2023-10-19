from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'gerente'

urlpatterns = [
    path('pagina_inicial/<str:cpf_gerente>/', pagina_inicial, name='pagina_inicial'),
    path('aprovar_concessao/<int:concessao_id>/<int:decisao>', aprovar_concessao, name='aprovar_concessao'),
    #path('listar_produtos/', name='listar_produtos' ),
    #path('produto_detalhes/<int:pk>)', name="produto_detalhes")
]