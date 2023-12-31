from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect
from .forms import EmprestimoForm, FinanciamentoForm, ConsorcioForm
from django.utils import timezone
from datetime import timedelta

# Create your views here.

def emprestimo(request, numero_conta):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            valor_contratado = form.cleaned_data['valor_contratado']
            dias_primeiro_vencimento = int(form.cleaned_data['data_primeiro_vencimento'])
            data_primeiro_vencimento = timezone.now().date() + timedelta(days=dias_primeiro_vencimento)
            qtd_parcelas = form.cleaned_data['qtd_parcelas']
            valor_total_pago = form.cleaned_data['valor_total_pago']
            taxa_juros = form.cleaned_data['taxa_juros']
            valor_parcela = form.cleaned_data['valor_parcela']

            # adicionar depois o mesmo calculo para verificar se nao teve alteração no front

            # recupera o cpf do cliente e o cpf do gerente pelo numero da conta
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT cliente_id, gerente_id FROM conta_conta_bancaria WHERE numero = '{numero_conta}'""")
                cliente_cpf, gerente_cpf = cursor.fetchone()
            
            # insere a concessao no banco de dados
            with connection.cursor() as cursor:
                try:
                    cursor.execute(f"""INSERT INTO concessao_concessao 
                                        (cliente_id, conta_id, produto_id, gerente_id, valor_contratado, 
                                        data_primeiro_vencimento, qtd_parcelas, juros, valor_parcela, 
                                        valor_total, status) 
                                        VALUES ('{cliente_cpf}', '{numero_conta}', '1', '{gerente_cpf}', '{valor_contratado}', 
                                                '{data_primeiro_vencimento}', '{qtd_parcelas}', '{taxa_juros}', '{valor_parcela}', 
                                                '{valor_total_pago}', 'Em Analise')""")
                    return redirect('produto:emprestimos_conta', numero_conta=numero_conta)
                except Exception as e:
                    print(e)
                    return render(request, 'form_emprestimo.html',{'form': form, 'erro': e})
        else:
            erros = form.errors
            print(erros)
            return render(request, 'form_emprestimo.html',{'form': form, 'erro': erros})
    else:
        form = EmprestimoForm()
        return render(request, 'form_emprestimo.html',{'form': form, 'numero': numero_conta})

def financiamento(request, numero_conta):
    if request.method == 'POST':
        form = FinanciamentoForm(request.POST)
        if form.is_valid():
            valor_contratado = form.cleaned_data['valor_contratado']
            dias_primeiro_vencimento = int(form.cleaned_data['data_primeiro_vencimento'])
            data_primeiro_vencimento = timezone.now().date() + timedelta(days=dias_primeiro_vencimento)
            qtd_parcelas = form.cleaned_data['qtd_parcelas']
            valor_total_pago = form.cleaned_data['valor_total_pago']
            taxa_juros = form.cleaned_data['taxa_juros']
            valor_parcela = form.cleaned_data['valor_parcela']

            # adicionar depois o mesmo calculo para verificar se nao teve alteração no front

            # recupera o cpf do cliente e o cpf do gerente pelo numero da conta
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT cliente_id, gerente_id FROM conta_conta_bancaria WHERE numero = '{numero_conta}'""")
                cliente_cpf, gerente_cpf = cursor.fetchone()
            
            # insere a concessao no banco de dados
            with connection.cursor() as cursor:
                try:
                    cursor.execute(f"""INSERT INTO concessao_concessao 
                                        (cliente_id, conta_id, produto_id, gerente_id, valor_contratado, 
                                        data_primeiro_vencimento, qtd_parcelas, juros, valor_parcela, 
                                        valor_total, status) 
                                        VALUES ('{cliente_cpf}', '{numero_conta}', '3', '{gerente_cpf}', '{valor_contratado}', 
                                                '{data_primeiro_vencimento}', '{qtd_parcelas}', '{taxa_juros}', '{valor_parcela}', 
                                                '{valor_total_pago}', 'Em Analise')""")
                    return redirect('produto:financiamentos_conta', numero_conta=numero_conta)
                except Exception as e:
                    print(e)
                    return render(request, 'form_financiamento.html',{'form': form, 'erro': e})
        else:
            erros = form.errors
            print(erros)
            return render(request, 'form_financiamento.html',{'form': form, 'erro': erros})
    else:
        form = FinanciamentoForm()
        return render(request, 'form_financiamento.html',{'form': form, 'numero': numero_conta})

def consorcio(request, numero_conta):
    if request.method == 'POST':
        form = ConsorcioForm(request.POST)
        if form.is_valid():
            valor_contratado = form.cleaned_data['valor_contratado']
            dias_primeiro_vencimento = int(form.cleaned_data['data_primeiro_vencimento'])
            data_primeiro_vencimento = timezone.now().date() + timedelta(days=dias_primeiro_vencimento)
            qtd_parcelas = form.cleaned_data['qtd_parcelas']
            valor_total_pago = form.cleaned_data['valor_total_pago']
            taxa_juros = form.cleaned_data['taxa_juros']
            valor_parcela = form.cleaned_data['valor_parcela']

            # adicionar depois o mesmo calculo para verificar se nao teve alteração no front

            # recupera o cpf do cliente e o cpf do gerente pelo numero da conta
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT cliente_id, gerente_id FROM conta_conta_bancaria WHERE numero = '{numero_conta}'""")
                cliente_cpf, gerente_cpf = cursor.fetchone()
            
            # insere a concessao no banco de dados
            with connection.cursor() as cursor:
                try:
                    cursor.execute(f"""INSERT INTO concessao_concessao 
                                        (cliente_id, conta_id, produto_id, gerente_id, valor_contratado, 
                                        data_primeiro_vencimento, qtd_parcelas, juros, valor_parcela, 
                                        valor_total, status) 
                                        VALUES ('{cliente_cpf}', '{numero_conta}', '2', '{gerente_cpf}', '{valor_contratado}', 
                                                '{data_primeiro_vencimento}', '{qtd_parcelas}', '{taxa_juros}', '{valor_parcela}', 
                                                '{valor_total_pago}', 'Em Analise')""")
                    return redirect('produto:consorcios_conta', numero_conta=numero_conta)
                except Exception as e:
                    print(e)
                    return render(request, 'form_consorcio.html',{'form': form, 'erro': e})
        else:
            erros = form.errors
            print(erros)
            return render(request, 'form_consorcio.html',{'form': form, 'erro': erros})
    else:
        form = ConsorcioForm()
        return render(request, 'form_consorcio.html',{'form': form, 'numero': numero_conta})
    
def historico_concessao(request):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT * FROM concessao WHERE id_cliente = '{request.user.id_cliente}'""")
    return cursor.fetchall()