import psycopg2
import os

def senha_banco():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.join(base_dir, '..', 'senha_banco.txt')
        with open(caminho) as senha_banco:
            senha = senha_banco.read()
        return senha
    except FileNotFoundError:
        print('Arquivo não encontrado')
        return None


def criar_conexao():
    dbname = 'zenith_capital'
    user = 'postgres'
    password = senha_banco()
    host = 'localhost'
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )
        print("Conexão bem-sucedida!")
        return conn
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None
    
if __name__ == '__main__':
    criar_conexao()
        