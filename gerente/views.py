from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.
def pagina_inicial(request, cpf_gerente):
    # recupera todas as concessoes em analise
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT * FROM concessao_concessao WHERE status = 'Em Analise' and gerente_id = {cpf_gerente}""")
        concessoes = cursor.fetchall()
    
    # recupera as informações do cliente e da conta
    nova_lista = []
    for concessao in concessoes:
        conc = list(concessao)
        cpf_cliente = concessao[8]
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM cliente_cliente WHERE cpf = {cpf_cliente}""")
            cliente = cursor.fetchone()
        conc.append(cliente)
        numero_conta = concessao[9]
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM conta_conta_bancaria WHERE numero = {numero_conta}""")
            conta = cursor.fetchone()
        conc.append(conta)
        
        # recupera a quantidade de produtos que o cliente tem aprovado
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT nome, count(produto_id)
                                FROM concessao_concessao 
                                join produto_produto on produto_id = produto
                                WHERE status = 'Aprovado' and cliente_id = {cpf_cliente}
                                group by nome
                                """)
            produtos_contratados = cursor.fetchall()
        conc.append(produtos_contratados)
        nova_lista.append(conc)
    
    return render(request, 'pagina_inicial_gerente.html', {'concessoes': nova_lista, 'gerente': True,})


def aprovar_concessao(request, concessao_id, decisao):
    # altera o status da concessao para aprovado
    if decisao == 1:
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"""UPDATE concessao_concessao SET status = 'Aprovado' WHERE concessao = {concessao_id}""")
                cursor.execute(f"""SELECT * FROM concessao_concessao WHERE concessao = {concessao_id}""")
                concessao = cursor.fetchone()
                numero_conta = concessao[9]
                valor = concessao[1]
                cursor.execute(f"""UPDATE conta_conta_bancaria SET saldo = saldo + {valor} WHERE numero = {numero_conta}""")
                if concessao[11] == 1:
                    descricao = 'Produto:Emprestimo'
                elif concessao[11] == 2:
                    descricao = 'Produto:Financiamento'
                else:
                    descricao = 'Produto:Consorcio'
                cursor.execute(f"""INSERT INTO conta_transacao (tipo, conta_id, valor, descricao, data_hora)
                                                VALUES ('entrada', {numero_conta}, {valor}, '{descricao}', '{timezone.now()}')
                                                """)
        except:
            return redirect('gerente:pagina_inicial', cpf_gerente=concessao[10], error='Erro ao aprovar concessão')
        else:
            return redirect('gerente:pagina_inicial', cpf_gerente=concessao[10])
    else:
        with connection.cursor() as cursor:
            cursor.execute(f"""UPDATE concessao_concessao SET status = 'Reprovado' WHERE concessao = {concessao_id}""")
            cursor.execute(f"""SELECT gerente_id FROM concessao_concessao WHERE concessao = {concessao_id}""")
            concessao = cursor.fetchone()
            return redirect('gerente:pagina_inicial', cpf_gerente=concessao[0])

