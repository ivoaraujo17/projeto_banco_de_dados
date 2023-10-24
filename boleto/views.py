from django.shortcuts import render
from django.db import connection
from .form import BoletoForm
from django.shortcuts import redirect
# Create your views here.
def boletos(request, numero_conta):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM boleto_boleto WHERE conta_id = %s', [numero_conta])
        boletos = cursor.fetchall()
        print(boletos)
    return render(request, 'boletos_deposito.html', {'numero': numero_conta, 'boletos': boletos})

def criar_boleto(request, numero_conta):
    if request.method == 'POST':
        form = BoletoForm(request.POST)
        if form.is_valid():
            valor = form.cleaned_data['valor']
            data_vencimento = form.cleaned_data['data_vencimento']
            # gera uma sequencia de 10 numeros aleatorios
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO boleto_boleto (valor, data_vencimento, conta_id, pago) VALUES (%s, %s, %s, %s)', [valor, data_vencimento, numero_conta, False])
            return redirect('conta_bancaria:boleto:depositar', numero_conta=numero_conta)
    else:
        form = BoletoForm()
        return render(request, 'form_boletos.html', {'numero': numero_conta, 'form': form})