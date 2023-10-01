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

    """
        if (nome=="" and email=="" and telefone=="" and data_nascimento=="" and nacionalidade=="" and estado_civil=="" and 
        renda_mensal=="" and logradouro=="" and bairro=="" and cidade=="" and estado=="" and cep==""):
        print("entrou no if tudo vazio")
        pass
    else:
        print("Entrou no else, nao esta vazio")   
        ultima_atualizacao = datetime.now().strftime('%d-%m-%Y')
    """
    ultima_atualizacao = datetime.now().strftime('%d-%m-%Y')

    

    # Verificando se o nome deve ser alterado e alterando-0
    if nome != "" and type(nome) == str:
        cliente[1] = nome
    
    # Verificando se o email deve ser alterado e alterando-0
    if email != "":
        try:
            emailinfo = validate_email(email, check_deliverability=False)
            email = emailinfo.normalized
            cliente[2] = email
        except EmailNotValidError as e:
            return [False, "Email inválido"]
    
    # Verificando se o telefone deve ser alterado e alterando-0   
    if telefone != "":
        if trata_telefone(telefone)[0] == False:
            return [False, "Telefone inválido"]
        else:
            telefone = trata_telefone(telefone)[1]
            cliente[3] = telefone

    # Verificando se a data de nascimento deve ser alterada e alterando-a
    if data_nascimento != "":
        if not datetime.strptime(data_nascimento, '%d-%m-%Y'):
            return [False, "Data de nascimento inválida"]
        else:
            cliente[4] = data_nascimento
    
    # Verificando se a nacionalidade deve ser alterada e alterando-a
    if nacionalidade != "" and type(nacionalidade) == str:
        cliente[5] = nacionalidade
    
    # Verificando se o estado civil deve ser alterado e alterando-o
    if estado_civil != "" and type(estado_civil) == str:
        cliente[6] = estado_civil
    
    # Verificando se a renda mensal deve ser alterada e alterando-a
    if renda_mensal != "":
        try:
            print("Tentando converter a renda")
            renda_mensal = float(renda_mensal)
            print("Renda convertida")
            if renda_mensal > 0:
                print("Tentando atribuir a renda a coluna")
                cliente[7] = renda_mensal
                print("Renda atribuida a coluna")
                return [True, renda_mensal]
            else:
                return [False, "Renda mensal inválida"]
        except:
            print("Formato de renda invalido.")
            return [False, "Renda mensal inválida"]
        
    
    # Verificando se o logradouro deve ser alterado e alterando-o
    if logradouro != "" and type(logradouro) == str:
        cliente[8] = logradouro
    
    # Verificando se o bairro deve ser alterado e alterando-o
    if bairro != "" and type(bairro) == str:
        cliente[9] = bairro
    
    # Verificando se a cidade deve ser alterada e alterando-a
    if cidade != "" and type(cidade) == str:
        cliente[10] = cidade
    
    # Verificando se o estado deve ser alterado e alterando-o
    if estado != "" and type(estado) == str:
        cliente[11] = estado
    
    # Verificando se o cep deve ser alterado e alterando-o
    if cep != "":
        if len(cep) != 8:
            return [False, "CEP inválido"]
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

    

