from conexao_banco import criar_conexao

def listar_todos():
    com = criar_conexao()
    cursor = com.cursor()

    return cursor.execute(f""" SELECT * FROM private.cliente """)

def pesquisar_por_nome(nome_desejado):
    com = criar_conexao()
    cursor = com.cursor()

    return cursor.execute(f""" SELECT * FROM private.cliente WHERE nome = '{nome_desejado}' """)

#Exibir um do que exatamente?