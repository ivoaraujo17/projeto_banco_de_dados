from crud import Crud

crud = Crud()

#criar_cliente(self, cpf, nome, email, telefone, data_nascimento, nacionalidade, 
#                       estado_civil, renda_mensal, logradouro, bairro, cidade, 
#                        estado, cep, data_entrada=""):

"""criado = crud.criar_cliente("61390611051", "Paulo", "paulo@gmail.com", "83976653214", "14-06-1998", "brasileiro", "solteiro",
                   3000.01, "Rua jonas burgo", "Blightown", "são paulo", 
                  "são paulo", "43423443", "29-09-2023")"""

#atualizado = crud.atualizar_cliente('83754444050', 'Andre', 'flamengo@gmail.com', '83998604080', '14-06-1988', 'estrangeiro', 'casado', 
# 6800.34, 'Rua do Piao Azul, 81', 'Majula', 'Farinha vermelha', 'Tocantins', '98043220')

atualizado2 = crud.atualizar_cliente('83754444050', email= 'vasco@gmail.com')




""""
print(crud.pesquisar_por_nome("Paulo"))
print(crud.pesquisar_por_cpf("61390611051"))

print(crud.pesquisar_por_nome("Andre"))
print(crud.pesquisar_por_cpf("83754444050"))"""

print(crud.listar_todos_clientes())