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
    
    
    