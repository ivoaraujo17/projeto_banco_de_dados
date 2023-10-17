from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect
from .forms import EmprestimoForm, FinanciamentoForm, ConsorcioForm

# Create your views here.

def emprestimo(request):
    if request.method == 'POST':
        pass
    else:
        form = EmprestimoForm()
        return render(request, 'form_emprestimo.html',{'form': form})

def financiamento(request):
    if request.method == 'POST':
        pass
    else:
        form = FinanciamentoForm()
        return render(request, 'form_financiamento.html',{'form': form})

def consorcio(request):
    if request.method == 'POST':
        pass
    else:
        form = ConsorcioForm()
        return render(request, 'form_consorcio.html',{'form': form})

def solicitar_concessao(request):
    
    return

def historico_concessao(request):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT * FROM concessao WHERE id_cliente = '{request.user.id_cliente}'""")
        historico = cursor.fetchall()
    return