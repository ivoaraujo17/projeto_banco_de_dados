from django.shortcuts import render
from django.db import connection, transaction
from django.db.utils import OperationalError, IntegrityError
from django.shortcuts import redirect
from .forms import *
from django.utils import timezone

# Create your views here.

def escolha_tipo_conta(request):
    return render(request, 'escolha_tipo_conta.html')

def pagina_inicial(request):
    # Verificar se o cliente já tem uma conta
    with connection.cursor() as cursor:
        # busca o cpf do cliente logado
        cursor.execute("SELECT cpf FROM cliente_cliente WHERE email = %s", [request.user.email])
        cpf = cursor.fetchone()
        if cpf == None:
            return redirect('cliente:cadastro_cliente')
        else:
            cpf = cpf[0]
        cursor.execute("SELECT numero FROM conta_conta_bancaria WHERE cliente_id = %s", [cpf])
        contas = cursor.fetchall()

    if contas:
        if len(contas) == 1:
            return redirect('conta_bancaria:minha_conta', numero_conta=contas[0][0])
        else:
            return redirect('conta_bancaria:escolha_tipo_conta')
    else:
        return redirect('conta_bancaria:escolha_tipo_conta')

def criar_conta_corrente(request):
    # verifica se o cliente ja tem uma conta corrente
    with connection.cursor() as cursor:
        # busca o cpf do cliente logado
        cursor.execute("SELECT cpf FROM cliente_cliente WHERE email = %s", [request.user.email])
        cpf = cursor.fetchone()[0]
        # busca o numero de contas correntes do cliente
        cursor.execute("SELECT numero FROM conta_conta_bancaria WHERE cliente_id = %s AND tipo_conta = 'Corrente'", [cpf])
        conta_corrente = cursor.fetchone()
    
    if conta_corrente:
        return redirect('conta_bancaria:minha_conta', numero_conta=conta_corrente[0])
    else:
        # insere a conta no banco de dados
        with connection.cursor() as cursor:
            # busca um gerente do mesmo estado do cliente, caos não exista, busca um gerente de outro estado
            cursor.execute("SELECT cpf FROM gerente_gerente WHERE estado = (SELECT estado FROM cliente_cliente WHERE cpf = %s)", [cpf])
            gerente = cursor.fetchone()
            if gerente == None:
                cursor.execute("SELECT cpf FROM gerente_gerente")
                # busca a quantidade de gerentes
                gerentes = cursor.fetchall()
                qtd_gerentes = len(gerentes)
                # gera um numero aleatorio entre 0 e a quantidade de gerentes
                import random
                n = random.randint(0, qtd_gerentes -1)
                gerente = gerentes[n][0]
            else:
                gerente = gerente[0]

            cursor.execute("INSERT INTO conta_conta_bancaria (cliente_id, tipo_conta, agencia, gerente_id, saldo, limite_especial) VALUES (%s, %s, %s, %s, %s, %s)", 
                            [cpf, 'Corrente', 1001, gerente, 0, 0])
            
            # busca o numero da conta corrente
            cursor.execute("SELECT numero FROM conta_conta_bancaria WHERE cliente_id = %s AND tipo_conta = 'Corrente'", [cpf])
            conta_corrente = cursor.fetchone()
        
        return redirect('conta_bancaria:minha_conta', numero_conta=conta_corrente[0])

def criar_conta_poupanca(request):
    # verifica se o cliente ja tem uma conta poupança
    with connection.cursor() as cursor:
        # busca o cpf do cliente logado
        cursor.execute("SELECT cpf FROM cliente_cliente WHERE email = %s", [request.user.email])
        cpf = cursor.fetchone()[0]
        # busca o numero de contas poupanças do cliente
        cursor.execute("SELECT numero FROM conta_conta_bancaria WHERE cliente_id = %s AND tipo_conta = 'Poupança'", [cpf])
        conta_poupanca = cursor.fetchone()
    
    if conta_poupanca:
        return redirect('conta_bancaria:minha_conta', numero_conta=conta_poupanca[0])
    else:
        # insere a conta no banco de dados
        with connection.cursor() as cursor:
            # busca um gerente do mesmo estado do cliente, caos não exista, busca um gerente de outro estado
            cursor.execute("SELECT cpf FROM gerente_gerente WHERE estado = (SELECT estado FROM cliente_cliente WHERE cpf = %s)", [cpf])
            gerente = cursor.fetchone()
            if gerente == None:
                cursor.execute("SELECT cpf FROM gerente_gerente")
                # busca a quantidade de gerentes
                gerentes = cursor.fetchall()
                qtd_gerentes = len(gerentes)
                # gera um numero aleatorio entre 0 e a quantidade de gerentes
                import random
                n = random.randint(0, qtd_gerentes -1)
                gerente = gerentes[n][0]
            else:
                gerente = gerente[0]


            cursor.execute("""INSERT INTO conta_conta_bancaria 
                            (cliente_id, tipo_conta, agencia, 
                            gerente_id, saldo, limite_especial) 
                            VALUES (%s, %s, %s, %s, %s, %s)""", 
                            [cpf, 'Poupança', 1001, gerente, 0, 0])
            # busca o numero da conta poupança
            cursor.execute("SELECT numero FROM conta_conta_bancaria WHERE cliente_id = %s AND tipo_conta = 'Poupança'", [cpf])
            conta_poupanca = cursor.fetchone()

        return redirect('conta_bancaria:minha_conta', numero_conta=conta_poupanca[0])

def criar_conta_salario(request):
    # verifica se o cliente ja tem uma conta salario
    with connection.cursor() as cursor:
        # busca o cpf do cliente logado
        cursor.execute("SELECT cpf FROM cliente_cliente WHERE email = %s", [request.user.email])
        cpf = cursor.fetchone()[0]
        # busca o numero de contas salario do cliente
        cursor.execute("SELECT numero FROM conta_conta_bancaria WHERE cliente_id = %s AND tipo_conta = 'Salario'", [cpf])
        conta_salario = cursor.fetchone()
    
    if conta_salario:
        return redirect('conta_bancaria:minha_conta', numero_conta=conta_salario[0])
    else:
        # insere a conta no banco de dados
        with connection.cursor() as cursor:
            # busca um gerente do mesmo estado do cliente, caos não exista, busca um gerente de outro estado
            cursor.execute("SELECT cpf FROM gerente_gerente WHERE estado = (SELECT estado FROM cliente_cliente WHERE cpf = %s)", [cpf])
            gerente = cursor.fetchone()
            if gerente == None:
                cursor.execute("SELECT cpf FROM gerente_gerente")
                # busca a quantidade de gerentes
                gerentes = cursor.fetchall()
                qtd_gerentes = len(gerentes)
                # gera um numero aleatorio entre 0 e a quantidade de gerentes
                import random
                n = random.randint(0, qtd_gerentes -1)
                gerente = gerentes[n][0]
            else:
                gerente = gerente[0]


            cursor.execute("""INSERT INTO conta_conta_bancaria 
                            (cliente_id, tipo_conta, agencia, 
                            gerente_id, saldo, limite_especial) 
                            VALUES (%s, %s, %s, %s, %s, %s)""", 
                            [cpf, 'Salario', 1001, gerente, 0, 0])

            cursor.execute("SELECT numero FROM conta_conta_bancaria WHERE cliente_id = %s AND tipo_conta = 'Salario'", [cpf])
            conta_salario = cursor.fetchone()

        return redirect('conta_bancaria:minha_conta', numero_conta=conta_salario[0])

def minha_conta(request, numero_conta):
    # busca os dados da conta
    with connection.cursor() as cursor:
        cursor.execute("""SELECT numero, agencia, tipo_conta, saldo, limite_especial, cliente_id, gerente_id
                            FROM conta_conta_bancaria 
                            WHERE numero = %s""", 
                            [numero_conta])
        conta = cursor.fetchone()
    
    # busca o cpf do cliente logado e compara com  o dono  da conta
    with connection.cursor() as cursor:
        cursor.execute("SELECT cpf FROM cliente_cliente WHERE email = %s", [request.user.email])
        cpf = cursor.fetchone()[0]

    return render(request, 'pagina_inicial_conta.html', 
                    {'numero': conta[0],
                    'agencia': conta[1],
                    'tipo_conta': conta[2],
                    'saldo': conta[3],
                    'limite_especial': conta[4],
                    'cliente': conta[5],
                    'gerente': conta[6],
                    }
                    )

def transferencia(request, numero_conta):
    if request.method == 'POST':
        form = FormTransferencia(request.POST)
        if form.is_valid():
            conta_destino = form.cleaned_data['numero_conta']
            valor = form.cleaned_data['valor']
            if valor <= 0:
                    return render(request, 'form_transferencia.html', 
                                    {'form': form, 'mensagem':'Valor inválido', 'numero':numero_conta})
            # busca a conta destino e o saldo da conta atual 
            with connection.cursor() as cursor:
                cursor.execute("SELECT saldo FROM conta_conta_bancaria WHERE numero = %s", [conta_destino])
                saldo_conta_destino = cursor.fetchone()
                cursor.execute("SELECT saldo FROM conta_conta_bancaria WHERE numero = %s", [numero_conta])
                saldo_conta = cursor.fetchone()
            # verifica se as contas existem
            if saldo_conta_destino:
                saldo_conta_destino = saldo_conta_destino[0]
                saldo = saldo_conta[0]
                if saldo < valor:
                    return render(request, 'form_transferencia.html', 
                                    {'form': form, 'mensagem':'Você não possui saldo suficiente para realizar a transação!', 'numero':numero_conta})
                # lanca a saida em transferencias da conta atual e a entrada na conta destino, atualizando os saldos
                try:
                    with transaction.atomic():
                        with connection.cursor() as cursor:
                            cursor.execute(f"""INSERT INTO conta_transacao (tipo, conta_id, valor, descricao, data_hora)
                                                VALUES ('saida', {numero_conta}, {valor}, '{'transferencia:conta:' + str(conta_destino)}', '{timezone.now()}')
                                                """)
                            cursor.execute(f"""INSERT INTO conta_transacao (tipo, conta_id, valor, descricao, data_hora)
                                                VALUES ('entrada', {conta_destino}, {valor}, '{'transferencia:conta:' + str(numero_conta)}', '{timezone.now()}')
                                                """)
                        return redirect('conta_bancaria:extrato', numero_conta)
                except IntegrityError as e:
                    transaction.set_rollback(True)
                    return render(request, 'form_transferencia.html', 
                                    {'form': form, 'mensagem':'Erro ao realizar a transação, tente novamente!', 'numero':numero_conta})
            else:
                return render(request, 'form_transferencia.html', 
                                {'form': form, 'mensagem':'Conta destino não existe, verifique o número!', 'numero':numero_conta})    
        else:
            return render(request, 'form_transferencia.html',
                                    {'form': form, 'mensagem':'Formulário invalido', 'numero':numero_conta})
    else:
        form = FormTransferencia()
        return render(request, 'form_transferencia.html', {'form':form, 'numero':numero_conta})

def extrato(request, numero_conta):
    # busca a conta
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM conta_transacao WHERE conta_id = %s", [numero_conta])
        transacoes = cursor.fetchall()
    return render(request, 'extrato.html', {'transacoes':transacoes, 'numero':numero_conta})
