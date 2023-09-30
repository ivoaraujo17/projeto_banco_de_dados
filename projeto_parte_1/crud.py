from conexao_banco import criar_conexao
from create import create_cliente

class Crud():

    def __init__(self) -> None:
        conexao = criar_conexao()
        conexao.cursor()
        

    
    def create_cliente(self, cpf, nome, email, telefone, data_nascimento, nacionalidade, 
                       estado_civil, renda_mensal, logradouro, bairro, cidade, 
                        estado, cep, data_entrada=""):
        create_cliente(self.cursor, cpf, nome, email, telefone, data_nascimento, 
                   nacionalidade, estado_civil, renda_mensal, logradouro, bairro, cidade, 
                   estado, cep, data_entrada)
        


crud = Crud()
print(crud.create_cliente('12843361400', 'ivo', 'ivo.araujo@gmail.com', '83993515048',
                    '30/05/2001', 'brasileiro', 'solteiro', 2000, 
                    'rua professora luzia de crsto', 'valentina', 'joao pessoa', 'pb', '58254-00',
                    '30/09/2023'))
