from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect

# Create your views here.

def solicitar_concessao(request):
    
    return

def historico_concessao(request):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT * FROM concessao WHERE id_cliente = '{request.user.id_cliente}'""")
        historico = cursor.fetchall()
    return