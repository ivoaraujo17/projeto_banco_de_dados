from conexao_banco import criar_conexao
#crie uma função que deleta uma linha em banco de dados
def deletar_cliente(cpf):
    #cria uma conexão com o banco de dados
    conn = criar_conexao()
    #cria um cursor para executar comandos no banco de dados
    cursor = conn.cursor()
    #cria uma string com o comando SQL para deletar um cliente
    #crie um tratamento de erro para o caso de o cpf não existir no banco de dados
    try:
        cursor.execute(f"""DELETE FROM private.cliente WHERE cpf = '{cpf}';""")
        conn.commit()
        cursor.close()
        conn.close()
        return [True, "Cliente deletado com sucesso"]
    except:
        cursor.close()
        conn.close()
        return [False, "Cliente não encontrado"]
    
    
    