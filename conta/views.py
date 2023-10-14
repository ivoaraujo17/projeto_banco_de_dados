from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect

# Create your views here.

def escolha_tipo_conta(request):
    return render(request, 'escolha_tipo_conta.html')

def pagina_inicial(request):
    # Verificar se o cliente já tem uma conta
    with connection.cursor() as cursor:
        # busca o cpf do cliente logado
        cursor.execute("SELECT cpf FROM cliente_cliente WHERE email = %s", [request.user.email])
        cpf = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM conta_conta_bancaria WHERE cliente_id = %s", [cpf])
        contas = cursor.fetchone()[0]
    if contas  == 1:
        return render(request, 'pagina_inicial_conta.html')
    elif contas > 1:
        #mudar depois para uma página de escolha de conta
        return render(request, 'pagina_inicial_conta.html')
    else:
        return redirect('conta_bancaria:escolha_tipo_conta')


def criar_conta_corrente(request):
    # verifica se o cliente ja tem uma conta corrente
    cpf = None
    with connection.cursor() as cursor:
        # busca o cpf do cliente logado
        cursor.execute("SELECT cpf FROM cliente_cliente WHERE email = %s", [request.user.email])
        cpf = cursor.fetchone()[0]
        # busca o numero de contas correntes do cliente
        cursor.execute("SELECT COUNT(*) FROM conta_conta_bancaria WHERE cliente_id = %s AND tipo_conta = 'Corrente'", [cpf])
        conta_corrente = cursor.fetchone()[0]
    
    if conta_corrente == 1:
        return render(request, 'pagina_inicial_conta.html', {'erro': 'Você já possui uma conta corrente.'})
    else:
        # insere a conta no banco de dados
        with connection.cursor() as cursor:
            # busca um gerente do mesmo estado do cliente, caos não exista, busca um gerente de outro estado
            cursor.execute("SELECT cpf FROM gerente_gerente WHERE estado = (SELECT estado FROM cliente_cliente WHERE cpf = %s)", [cpf])
            gerente = cursor.fetchone()[0]
            if gerente == None:
                cursor.execute("SELECT cpf FROM gerente_gerente")
                # busca a quantidade de gerentes
                qtd_gerentes = len(cursor.fetchall())
                # gera um numero aleatorio entre 0 e a quantidade de gerentes
                import random
                n = random.randint(0, qtd_gerentes -1)
                gerente = cursor.fetchone()[n]


            cursor.execute("INSERT INTO conta_conta_bancaria (cliente_id, tipo_conta, agencia, gerente_id, saldo, limite_especial) VALUES (%s, %s, %s, %s, %s, %s)", 
                            [cpf, 'Corrente', 1001, gerente, 0, 0])
        
        return redirect('conta_bancaria:pagina_inicial')

def criar_conta_poupanca(request):
    # verifica se o cliente ja tem uma conta poupança
    cpf = None
    with connection.cursor() as cursor:
        # busca o cpf do cliente logado
        cursor.execute("SELECT cpf FROM cliente_cliente WHERE email = %s", [request.user.email])
        cpf = cursor.fetchone()[0]
        # busca o numero de contas poupanças do cliente
        cursor.execute("SELECT COUNT(*) FROM conta_conta_bancaria WHERE cliente_id = %s AND tipo_conta = 'Poupança'", cpf)
        conta_poupanca = cursor.fetchone()[0]
    
    if conta_poupanca == 1:
        return render(request, 'pagina_inicial_conta.html', {'erro': 'Você já possui uma conta poupança.'})
    else:
        # insere a conta no banco de dados
        with connection.cursor() as cursor:
            # busca um gerente do mesmo estado do cliente, caos não exista, busca um gerente de outro estado
            cursor.execute("SELECT cpf FROM gerente_gerente WHERE estado = (SELECT estado FROM cliente_cliente WHERE cpf = %s)", [cpf])
            gerente = cursor.fetchone()[0]
            if gerente == None:
                cursor.execute("SELECT cpf FROM gerente_gerente")
                # busca a quantidade de gerentes
                qtd_gerentes = len(cursor.fetchall())
                # gera um numero aleatorio entre 0 e a quantidade de gerentes
                import random
                n = random.randint(0, qtd_gerentes -1)
                gerente = cursor.fetchone()[n]


            cursor.execute("""INSERT INTO conta_conta_bancaria 
                            (cliente_id, tipo_conta, agencia, 
                            gerente_id, saldo, limite_especial) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
                            [cpf, 'Poupança', 1001, gerente, 0, 0])
        
        return redirect('conta_bancaria:pagina_inicial')

def criar_conta_salario(request):
    # verifica se o cliente ja tem uma conta salario
    cpf = None
    with connection.cursor() as cursor:
        # busca o cpf do cliente logado
        cursor.execute("SELECT cpf FROM cliente_cliente WHERE email = %s", [request.user.email])
        cpf = cursor.fetchone()[0]
        # busca o numero de contas salario do cliente
        cursor.execute("SELECT COUNT(*) FROM conta_conta_bancaria WHERE cliente_id = '%s' AND tipo_conta = 'Salario'", cpf)
        conta_salario = cursor.fetchone()[0]
    
    if conta_salario == 1:
        return render(request, 'pagina_inicial_conta.html', {'erro': 'Você já possui uma conta salario.'})
    else:
        # insere a conta no banco de dados
        with connection.cursor() as cursor:
            # busca um gerente do mesmo estado do cliente, caos não exista, busca um gerente de outro estado
            cursor.execute("SELECT cpf FROM gerente_gerente WHERE estado = (SELECT estado FROM cliente_cliente WHERE cpf = %s)", [cpf])
            gerente = cursor.fetchone()[0]
            if gerente == None:
                cursor.execute("SELECT cpf FROM gerente_gerente")
                # busca a quantidade de gerentes
                qtd_gerentes = len(cursor.fetchall())
                # gera um numero aleatorio entre 0 e a quantidade de gerentes
                import random
                n = random.randint(0, qtd_gerentes -1)
                gerente = cursor.fetchone()[n]


            cursor.execute("""INSERT INTO conta_conta_bancaria 
                            (cliente_id, tipo_conta, agencia, 
                            gerente_id, saldo, limite_especial) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
                            [cpf, 'Salario', 1001, gerente, 0, 0])
        
        return redirect('conta_bancaria:pagina_inicial')