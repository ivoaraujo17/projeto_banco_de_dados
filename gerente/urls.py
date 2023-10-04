from django.contrib import admin
from django.urls import path



app_name = 'gerente'

urlpatterns = [
    path('listar_produtos/', name='listar_produtos' ),
    path('produto_detalhes/<int:pk>)', name="produto_detalhes")
]