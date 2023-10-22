from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect

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
    return render(request, 'consorcios_conta.html', {'numero': numero_conta, 'consorcios': consorcio})

def excluir_produto(request, concessao_id, numero_conta, produto_id):
    with connection.cursor() as cursor:
        cursor.execute(f"""DELETE FROM concessao_concessao WHERE concessao = '{concessao_id}'""")
    if produto_id == 1:
        return redirect('produto:emprestimos_conta', numero_conta=numero_conta)
    elif produto_id == 2:
        return redirect('produto:financiamentos_conta', numero_conta=numero_conta)
    elif produto_id == 3:
        return redirect('produto:consorcios_conta', numero_conta=numero_conta)
