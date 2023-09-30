from conexao_banco import criar_conexao
from create import create_cliente

class Crud():

    def __init__(self) -> None:
        self.conexao = criar_conexao()
        self.cursor = self.conexao.cursor()
        

    
    def create_cliente(self, cpf, nome, email, telefone, data_nascimento, nacionalidade, 
                       estado_civil, renda_mensal, logradouro, bairro, cidade, 
                        estado, cep, data_entrada=""):
        result = create_cliente(self.conexao, self.cursor, cpf, nome, email, telefone, data_nascimento, 
                   nacionalidade, estado_civil, renda_mensal, logradouro, bairro, cidade, 
                   estado, cep, data_entrada)
        return result
