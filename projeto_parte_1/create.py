from datetime import datetime
from validate_docbr import CPF
from email_validator import validate_email, EmailNotValidError
from phone_validate import trata_telefone
import psycopg2


def create_cliente(conexao, cursor, cpf, nome, email, telefone, data_nascimento, 
                   nacionalidade, estado_civil, renda_mensal, logradouro, bairro, cidade, 
                   estado, cep, data_entrada=""):
    validador_cpf  = CPF()

    # verifica se data_entrada é uma data válida, se valor for vazio ou se não for do tipo datetime, 
    # data_entrada recebe a data atual
    if data_entrada == "" or not type(data_entrada) == datetime:
        data_entrada = datetime.now().strftime('%d-%m-%Y')

    # data_atualizacao recebe a data atual
    ultima_atualizacao = datetime.now().strftime('%d-%m-%Y')

    # verifica se cpf é válido
    if not validador_cpf.validate(cpf):
        return [False, "CPF inválido"]
    
    # verifica se nome é vazio ou se não é do tipo string
    if nome == "" or not type(nome) == str:
        return [False, "Nome inválido"]
    
    # verifica se email é válido
    try:
        emailinfo = validate_email(email, check_deliverability=False)
        email = emailinfo.normalized
    except EmailNotValidError as e:
        return [False, "Email inválido"]
    
    # verifica se telefone é vazio ou se não é do tipo string
    if trata_telefone(telefone)[0] == False:
        return [False, "Telefone inválido"]
    else:
        telefone = trata_telefone(telefone)[1]

    # verifica se data_nascimento é uma data válida ou se não é do tipo datetime
    if not datetime.strptime(data_nascimento, '%d-%m-%Y'):
        return [False, "Data de nascimento inválida"]
    
    # verifica se nacionalidade é vazio ou se não é do tipo string
    if nacionalidade == "" or not type(nacionalidade) == str:
        return [False, "Nacionalidade inválida"]
    
    # verifica se estado_civil é vazio ou se não é do tipo string
    if estado_civil == "" or not type(estado_civil) == str:
        return [False, "Estado civil inválido"]
    
    # verifica se renda_mensal é vazio ou se não é do tipo float
    if renda_mensal == "" and not type(renda_mensal) == float and renda_mensal < 0:
        return [False, "Renda mensal inválida"]
    
    # verifica se logradouro é vazio ou se não é do tipo string
    if logradouro == "" or not type(logradouro) == str:
        return [False, "Logradouro inválido"]
    
    # verifica se bairro é vazio ou se não é do tipo string
    if bairro == "" or not type(bairro) == str:
        return [False, "Bairro inválido"]
    
    # verifica se cidade é vazio ou se não é do tipo string
    if cidade == "" or not type(cidade) == str:
        return [False, "Cidade inválida"]
    
    # verifica se estado é vazio ou se não é do tipo string
    if estado == "" or not type(estado) == str:
        return [False, "Estado inválido"]
    
    # verifica se cep é válido
    if len(cep) != 8:
        return [False, "CEP inválido"]

    # verifica se data_entrada é uma data válida ou se não é do tipo datetime
    if not datetime.strptime(data_entrada, '%d-%m-%Y'):
        return [False, "Data de nascimento inválida"]

    # cria o cliente no banco de dados
    try:
        cursor.execute(
            f"""INSERT INTO private.cliente (cpf, nome, email, telefone, data_nascimento, nacionalidade, estado_civil, 
                                    renda_mensal, logradouro, bairro, cidade, estado, cep, data_entrada, ultima_atualizacao)
            VALUES ('{cpf}', '{nome}', '{email}', '{telefone}', '{data_nascimento}', '{nacionalidade}', '{estado_civil}', 
                            {renda_mensal}, '{logradouro}', '{bairro}', '{cidade}', '{estado}', '{cep}', '{data_entrada}', 
                            '{ultima_atualizacao}'
                        );"""
                        )
        conexao.commit()
        return [True, "Cliente criado com sucesso"]
        
    except psycopg2.Error as erro:
        return [False, erro]
    
    
    