from conexao_banco import criar_conexao
#crie uma função que deleta uma linha em banco de dados
def deletar_cliente(cpf):
    #cria uma conexão com o banco de dados
    conn = criar_conexao()
    #cria um cursor para executar comandos no banco de dados
    cursor = conn.cursor()
    #cria uma string com o comando SQL para deletar um cliente
    comando_sql = f"""DELETE FROM private.cliente WHERE cpf = '{cpf}';"""
    #execute o comando SQL
    cursor.execute(comando_sql)
    #salva as alterações no banco de dados
    conn.commit()
    #fecha a conexão com o banco de dados
    conn.close()
    #retorne uma mensagem de sucesso
    return "Cliente deletado com sucesso"
    