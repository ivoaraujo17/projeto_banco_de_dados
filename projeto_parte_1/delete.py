from read import pesquisar_usando_cpf
import psycopg2

def delete_client(conn, cursor, cpf):
    pesquisa = pesquisar_usando_cpf(cursor, cpf)
    if not pesquisa[0]:
        return pesquisa
    
    try:
        cursor.execute(f"""DELETE FROM private.cliente WHERE cpf = '{cpf}';""")
        conn.commit()
        return [True, "Cliente deletado com sucesso"]
    except psycopg2.Error as erro:
        return [False, erro]
    
    
    