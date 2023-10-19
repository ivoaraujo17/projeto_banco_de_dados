from django.shortcuts import render
from django.db import connection

# Create your views here.

def emprestimos_conta(request, numero_conta):
    # recupera os emprestimos da conta
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT * FROM concessao_concessao WHERE conta_id = '{numero_conta}' and produto_id = 1""")
        emprestimos = cursor.fetchall()
    return render(request, 'emprestimos_conta.html', {'numero': numero_conta, 'emprestimos': emprestimos})

    