from conexao_banco import criar_conexao
from create import create_cliente
from update import update_cliente
from read import *
from delete import delete_client
from datetime import datetime
from validate_docbr import CPF
from email_validator import validate_email, EmailNotValidError
from phone_validate import trata_telefone

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
                        estado, cep):
        result = create_cliente(self.conexao, self.cursor, cpf, nome, email, telefone, data_nascimento, 
                   nacionalidade, estado_civil, renda_mensal, logradouro, bairro, cidade, 
                   estado, cep, data_entrada="")
        return result

    def validar_cpf(self, cpf):
        validador_cpf  = CPF()
        if not validador_cpf.validate(cpf):
            return [False, "CPF inválido"]
        else:
            return [True, cpf]
    
    def validar_nome(self, nome):
        if nome == "" or not type(nome) == str:
            return [False, "Nome inválido"]
        else:
            return [True, nome]
    
    def validar_email(self, email):
        try:
            emailinfo = validate_email(email, check_deliverability=False)
            email = emailinfo.normalized
        except EmailNotValidError as e:
            return [False, "Email inválido"]
        return [True, email]

    def validar_telefone(self, telefone):
        if trata_telefone(telefone)[0] == False:
            return [False, "Telefone inválido"]
        else:
            telefone = trata_telefone(telefone)[1]
            return [True, telefone]
    
    def validar_data_nascimento(self, data_nascimento):
        try:
            datetime.strptime(data_nascimento, '%d-%m-%Y')
            return [True, data_nascimento]
        except:
            return [False, "data de nascimento inválida."]

    def validar_nacionalidade(self, nacionalidade):
        if nacionalidade == "" or not type(nacionalidade) == str:
            return [False, "Nacionalidade inválida"]
        else:
            return [True, nacionalidade]
    
    def validar_estado_civil(self, estado_civil):
        if estado_civil == "" or not type(estado_civil) == str:
            return [False, "Estado civil inválido"]
        else:
            return [True, estado_civil]

    def validar_renda_mensal(self, renda_mensal):
        try:
            renda_mensal = float(renda_mensal)
            if renda_mensal > 0:
                return [True, renda_mensal]
            else:
                return [False, "Renda mensal inválida"]
        except:
            return [False, "Renda mensal inválida"]


    def validar_logradouro(self, logradouro):
        if logradouro == "" or not type(logradouro) == str:
            return [False, "Logradouro inválido"]
        else:
            return [True, logradouro]

    def validar_bairro(self, bairro):
        if bairro == "" or not type(bairro) == str:
            return [False, "Cidade inválida"]
        else:
            return [True, bairro]

    def validar_cidade(self, cidade):
        if cidade == "" or not type(cidade) == str:
            return [False, "Cidade inválida"]
        else:
            return [True, cidade]

    def validar_estado(self, estado):
        if estado == "" or not type(estado) == str:
            return [False, "Estado inválido"]
        else:
            return [True, estado]

    def validar_cep(self, cep):
        if len(cep) != 8:
            return [False, "CEP inválido"]
        else:
            return [True, cep]


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