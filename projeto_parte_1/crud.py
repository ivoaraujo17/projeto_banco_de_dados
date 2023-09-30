from conexao_banco import criar_conexao
from create import create_cliente
from update import update_cliente
from read import *
from delete import delete_client

class Crud():

    def __init__(self) -> None:
        self.conexao = criar_conexao()
        self.cursor = self.conexao.cursor()
        

    def __del__(self) -> None:
        if self.cursor:
            self.cursor.close()
    
        if self.conexao:
            self.conexao.close()

        
    def criar_cliente(self, cpf, nome, email, telefone, data_nascimento, nacionalidade, 
                       estado_civil, renda_mensal, logradouro, bairro, cidade, 
                        estado, cep, data_entrada=""):
        result = create_cliente(self.conexao, self.cursor, cpf, nome, email, telefone, data_nascimento, 
                   nacionalidade, estado_civil, renda_mensal, logradouro, bairro, cidade, 
                   estado, cep, data_entrada)
        return result


    def atualizar_cliente(self, cpf, nome="", email="", telefone="", data_nascimento="", nacionalidade="", estado_civil="", 
                    renda_mensal="", logradouro="", bairro="", cidade="", estado="", cep=""):
        result = update_cliente(self.conexao, self.cursor, cpf, nome, email, telefone, data_nascimento, 
                   nacionalidade, estado_civil, renda_mensal, logradouro, bairro, cidade, 
                   estado, cep)
        return result
    
    def listar_todos_clientes(self):
        return listar_todos(self.cursor)
    
    def pesquisar_por_nome(self, nome_desejado):
        return pesquisar_usando_nome(self.cursor, nome_desejado)
    
    def pesquisar_por_cpf(self, cpf_desejado):
        return pesquisar_usando_cpf(self.cursor, cpf_desejado)
            
    
    def deletar_cliente(self, cpf):
        result = delete_client(self.conexao, self.cursor, cpf)
        return result