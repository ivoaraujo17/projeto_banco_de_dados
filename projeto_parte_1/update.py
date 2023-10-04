from conexao_banco import criar_conexao
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
from phone_validate import trata_telefone
import psycopg2
from read import pesquisar_usando_cpf


def update_cliente(conexao_banco, cursor, cpf, nome="", email="", telefone="", data_nascimento="", nacionalidade="", estado_civil="", 
                    renda_mensal="", logradouro="", bairro="", cidade="", estado="", cep=""):
    
    pesquisa = pesquisar_usando_cpf(cursor, cpf)
    if not pesquisa[0]:
        return pesquisa
    # Selecionando o cliente pelo cpf
    cliente = list(pesquisa[1][0])

    # Data da atualização cadastral
    ultima_atualizacao = datetime.now().strftime('%d-%m-%Y')

    if nome != "":
        cliente[1] = nome
    if email != "":
        cliente[2] = email
    if telefone != "":
        cliente[3] = telefone
    if data_nascimento != "":
        cliente[4] = data_nascimento
    if nacionalidade != "":
        cliente[5] = nacionalidade
    if estado_civil != "":
        cliente[6] = estado_civil
    if renda_mensal != "":
        cliente[7] = renda_mensal
    if logradouro != "":
        cliente[8] = logradouro
    if bairro != "":
        cliente[9] = bairro
    if cidade != "":
        cliente[10] = cidade
    if estado != "":
        cliente[11] = estado
    if cep != "":
        cliente[12] = cep

    try:
        cursor.execute(
            f"""UPDATE private.cliente SET  nome = '{cliente[1]}',
                                            email = '{cliente[2]}',
                                            telefone = '{cliente[3]}',
                                            data_nascimento = '{cliente[4]}',
                                            nacionalidade = '{cliente[5]}',
                                            estado_civil = '{cliente[6]}',
                                            renda_mensal = {cliente[7]},
                                            logradouro = '{cliente[8]}',
                                            bairro = '{cliente[9]}',
                                            cidade = '{cliente[10]}',
                                            estado = '{cliente[11]}',
                                            cep = '{cliente[12]}',
                                            ultima_atualizacao = '{ultima_atualizacao}'
                WHERE cpf = '{cpf}';"""
                )
        conexao_banco.commit()
        return [True, "Cliente atualizado com sucesso!"]
    
    except psycopg2.Error as erro:
        return [False, erro]

    

