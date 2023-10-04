from validate_docbr import CPF
import psycopg2

def listar_todos(cursor):
    try:
        cursor.execute(f""" SELECT cpf, nome FROM private.cliente """)
        return [True, cursor.fetchall()]
    except psycopg2.Error as erro:
        return [False, erro]

def pesquisar_usando_nome(cursor, nome_desejado):
    if nome_desejado == "" or not type(nome_desejado) == str:
        return [False, "Nome inválido"]
    try:
        cursor.execute(f""" SELECT cpf, nome FROM private.cliente WHERE UPPER(nome) LIKE '%{nome_desejado}%' """)
        resultado = cursor.fetchall()
        if len(resultado) != 0:
            return [True, resultado]
        else:
            return [False, "Nome não encontrado"]
    except psycopg2.Error as erro:
        return [False, erro]
    
def pesquisar_usando_cpf(cursor, cpf_desejado):
    validador_cpf  = CPF()
    if not validador_cpf.validate(cpf_desejado):
        return [False, "CPF inválido"]
    try:
        cursor.execute(f""" SELECT * FROM private.cliente WHERE cpf = '{cpf_desejado}' """)
        resultado = cursor.fetchall()
        if len(resultado) != 0:
            return [True, resultado]
        else:
            return [False, "CPF não encontrado"]

    except psycopg2.Error as erro:
        return [False, erro]