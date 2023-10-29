from django.shortcuts import render
from django.db import connection
from .form import BoletoForm, PagarBoleto
from django.shortcuts import redirect
from django.utils import timezone
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

def pagar_boleto(request):
    if request.method == 'POST':
        form = PagarBoleto(request.POST)
        if form.is_valid():
            numero_boleto = form.cleaned_data['numero_boleto']
            #busca as informações do boleto
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM boleto_boleto WHERE numero = %s', [numero_boleto])
                boleto = cursor.fetchone()
            
            # se o boleto é valido
            if boleto:
                # se o boleto não foi pago
                if not boleto[5]:
                    # busca as informações da conta
                    with connection.cursor() as cursor:
                        cursor.execute('SELECT * FROM conta_conta_bancaria WHERE numero = %s', [boleto[4]])
                        conta = cursor.fetchone()
                        cursor.execute('UPDATE conta_conta_bancaria SET saldo = %s WHERE numero = %s', [conta[3]+boleto[1], conta[0]])
                        cursor.execute('UPDATE boleto_boleto SET pago = %s, data_pagamento = %s WHERE numero = %s', [True, timezone.now().date(), boleto[0]])
                        cursor.execute(f"""INSERT INTO conta_transacao (tipo, conta_id, valor, descricao, data_hora)
                                                VALUES ('entrada', {conta[0]}, {boleto[1]}, 'Boleto:Pagamento', '{timezone.now()}')
                                                """)    
                    return render(request, 'pagar_boleto.html', {'form': form, 'numero_boleto': numero_boleto, 'mensagem': 'Boleto pago com sucesso!'})
                else:
                    return render(request, 'pagar_boleto.html', {'form': form, 'numero_boleto': numero_boleto, 'mensagem': 'Boleto Ja foi pago!'})
            else:
                return render(request, 'pagar_boleto.html', {'form': form, 'numero_boleto': numero_boleto, 'mensagem': 'Boleto não existe!'})
        else:
            return render(request, 'pagar_boleto.html', {'form': form, 'mensagem': 'Formulario invalido!'})
    else:
        form = PagarBoleto()
        return render(request, 'pagar_boleto.html', {'form': form})
