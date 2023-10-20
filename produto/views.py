from django.shortcuts import render
from django.db import connection

# Create your views here.

def emprestimos_conta(request, numero_conta):
    # recupera os emprestimos da conta
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT * FROM concessao_concessao WHERE conta_id = '{numero_conta}' and produto_id = 1""")
        emprestimos = cursor.fetchall()
        print(emprestimos)
    return render(request, 'emprestimos_conta.html', {'numero': numero_conta, 'emprestimos': emprestimos})

def financiamentos_conta(request, numero_conta):
    # recupera os financiamentos da conta
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT * FROM concessao_concessao WHERE conta_id = '{numero_conta}' and produto_id = 2""")
        financiamentos = cursor.fetchall()
        print(financiamentos)
    return render(request, 'financiamentos_conta.html', {'numero': numero_conta, 'financiamentos': financiamentos})

def consorcios_conta(request, numero_conta):
    # recupera os consorcios da conta
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT * FROM concessao_concessao WHERE conta_id = '{numero_conta}' and produto_id = 3""")
        consorcio = cursor.fetchall()
        print(consorcio)
    return render(request, 'consorcio_conta.html', {'numero': numero_conta, 'consorcio': consorcio})
