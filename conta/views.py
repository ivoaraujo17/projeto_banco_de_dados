from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect

# Create your views here.

def escolha_tipo_conta(request):
    return render(request, 'escolha_tipo_conta.html')

def pagina_inicial(request):
    # Verificar se o cliente já tem uma conta
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM conta_conta_bancaria WHERE id_cliente_id = %s", [request.user.id])
        contas = cursor.fetchone()[0]

    if contas  == 1:
        return render(request, 'pagina_inicial_conta.html')
    elif contas > 1:
        #mudar depois para uma página de escolha de conta
        return render(request, 'pagina_inicial_conta.html')
    else:
        return redirect('conta_bancaria:escolha_tipo_conta')