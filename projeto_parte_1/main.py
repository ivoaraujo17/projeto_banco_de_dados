from crud import Crud

crud = Crud()
while True:
    resposta = int(input("Escolha uma operação para realizar:\n"
                    '(1) criar um cliente;\n'
                    '(2) atualizar um cliente;\n'
                    '(3) listar todos os clientes;\n'
                    '(4) pesquisar cliente por nome;\n'
                    '(5) exibir cliente por cpf;\n'
                    '(6) deletar um cliente;\n'))

    match resposta:  
        case 1:
            
            ccpf = crud.validar_cpf(input("Insira o cpf: \n"))
            while not ccpf[0]:
                ccpf = crud.validar_cpf(input("Cpf inválido. Insira o cpf: \n"))

            cnome = crud.validar_nome(input("Insira o nome: \n"))
            while not cnome[0]:
                cnome = crud.validar_nome(input("Nome inválido. Insira o nome: \n"))

            cemail = crud.validar_email(input("Insira o email: \n"))
            while not cemail[0]:
                cemail = crud.validar_email(input("Email inválido. Insira o email: \n"))

            ctelefone = crud.validar_telefone(input("Insira o telefone: \n"))
            while not ctelefone[0]:
                ctelefone = crud.validar_telefone(input("Telefone inválido. Insira o telefone: \n"))

            cdata_nascimento = crud.validar_data_nascimento(input("Insira a data de nascimento: \n"))
            while not cdata_nascimento[0]:
                cdata_nascimento = crud.validar_data_nascimento(input("Data de nascimento inválida. Insira a data de nascimento: \n"))

            cnacionalidade = crud.validar_nacionalidade(input("Insira a nacionalidade: \n"))
            while not cnacionalidade[0]:
                cnacionalidade = crud.validar_nacionalidade(input("Nacionalidade inválida. Insira a nacionalidade: \n"))

            cestado_civil = crud.validar_estado_civil(input("Insira o estado civil: \n"))
            while not cestado_civil[0]:
                cestado_civil = crud.validar_estado_civil(input("Estado civil inválido. Insira o estado civil: \n"))

            crenda_mensal = crud.validar_renda_mensal(input("Insira a renda mensal: \n"))
            while not crenda_mensal[0]:
                crenda_mensal = crud.validar_renda_mensal(input("Renda mensal inválida. Insira a renda mensal: \n"))

            clogradouro = crud.validar_logradouro(input("Insira o logradouro: \n"))
            while not clogradouro[0]:
                clogradouro = crud.validar_logradouro(input("Logradouro inválido. Insira o logradouro: \n"))

            cbairro = crud.validar_bairro(input("Insira o bairro: \n"))
            while not cbairro[0]:
                cbairro = crud.validar_bairro(input("Bairro inválido. Insira o bairro: \n"))

            ccidade = crud.validar_cidade(input("Insira a cidade: \n"))
            while not ccidade[0]:
                ccidade = crud.validar_cidade(input("Cidade inválida. Insira a cidade: \n"))

            cestado = crud.validar_estado(input("Insira o estado: \n"))
            while not cestado:
                cestado = crud.validar_estado(input("Estado inválido. Insira o estado: \n"))

            ccep = crud.validar_cep(input("Insira o CEP: \n"))
            while not ccep[0]:
                ccep = crud.validar_cep(input("CEP inválido. Insira o CEP: \n"))

            
            crud.criar_cliente(ccpf[1], cnome[1], cemail[1], ctelefone[1], cdata_nascimento[1], cnacionalidade[1], 
                        cestado_civil[1], crenda_mensal[1], clogradouro[1], cbairro[1], ccidade[1], 
                            cestado[1], ccep[1])
            print("Cliente criado!")

        case 2:
            
            procurando_cpf = crud.pesquisar_por_cpf(input("Insira o cpf de quem será alterado:"))
            while not procurando_cpf[0]:
                procurando_cpf = crud.pesquisar_por_cpf(input("CPF invalido. Insira o cpf de quem será alterado:"))
            
            cpf = procurando_cpf[1][0][0]
            nome=""
            email=""
            telefone=""
            data_nascimento=""
            nacionalidade=""
            estado_civil=""
            renda_mensal=""
            logradouro=""
            bairro=""
            cidade=""
            estado=""
            cep=""
            while True:
                campo = int(input("Digite o número correspondente ao campo que deve ser atualizado:\n"
                "1- nome\n"
                "2- email\n"
                "3- telefone\n"
                "4- data_nascimento\n"
                "5- nacionalidade\n"
                "6- estado_civil\n"
                "7- renda_mensal\n"
                "8- logradouro\n"
                "9- bairro\n"
                "10- cidade\n"
                "11- estado\n"
                "12- cep\n"
                "13- digite para sair\n"))
                match campo:
                    case 1:
                        campo_alterado = input("Digite o novo nome:")
                        #crud.atualizar_cliente(cpf, nome = campo_alterado)
                        nome = campo_alterado
                    case 2:
                        campo_alterado = input("Digite o novo email:")
                        #crud.atualizar_cliente(cpf, email = campo_alterado)
                        email = campo_alterado
                    case 3:
                        campo_alterado = input("Digite o novo telefone:")
                        #crud.atualizar_cliente(cpf, telefone = campo_alterado)
                        telefone = campo_alterado
                    case 4:
                        campo_alterado = input("Digite a nova data de nascimento:")
                        #crud.atualizar_cliente(cpf, data_nascimento = campo_alterado)
                        data_nascimento = campo_alterado
                    case 5:
                        campo_alterado = input("Digite a nova nacionalidade:")
                        #crud.atualizar_cliente(cpf, nacionalidade = campo_alterado)
                        nacionalidade = campo_alterado
                    case 6:
                        campo_alterado = input("Digite o novo estado civil:")
                        #crud.atualizar_cliente(cpf, estado_civil = campo_alterado)
                        estado_civil = campo_alterado
                    case 7:
                        campo_alterado = input("Digite a nova renda mensal:")
                        #crud.atualizar_cliente(cpf, renda_mensal = campo_alterado)
                        renda_mensal = campo_alterado
                    case 8:
                        campo_alterado = input("Digite o novo logradouro:")
                        #crud.atualizar_cliente(cpf, logradouro = campo_alterado)
                        logradouro = campo_alterado
                    case 9:
                        campo_alterado = input("Digite o novo bairro:")
                        #crud.atualizar_cliente(cpf, bairro = campo_alterado)
                        bairro = campo_alterado
                    case 10:
                        campo_alterado = input("Digite a nova cidade:")
                        #crud.atualizar_cliente(cpf, cidade = campo_alterado)
                        cidade = campo_alterado
                    case 11:
                        campo_alterado = input("Digite o novo estado:")
                        #crud.atualizar_cliente(cpf, estado = campo_alterado)
                        estado = campo_alterado
                    case 12:
                        campo_alterado = input("Digite o novo cep:")
                        #crud.atualizar_cliente(cpf, cep = campo_alterado)
                        cep = campo_alterado
                    case 13:
                        break
                    case _:
                        print("Opção inválida.")
                        
                continuar_atualizar = input("Deseja alterar outro campo? (s/n)")
                #Como está sendo alterado um campo por vez, esse break é utilizado quando não se deseja atualizar nenhum outro campo
                if continuar_atualizar.lower() != 's':
                    crud.atualizar_cliente(cpf, nome, email, telefone, data_nascimento, nacionalidade, estado_civil, 
                            renda_mensal, logradouro, bairro, cidade, estado, cep)
                    print("Cliente atualizado!")
                    break
                    
        case 3:
            print(crud.listar_todos_clientes())

        case 4:
            pesquisa_nome = input("Insira o nome para ser pesquisado: \n")
            print(crud.pesquisar_por_nome(pesquisa_nome))

        case 5:
            exibir_cpf = input("Insira o cpf para ser ser exibido: \n")
            print(crud.pesquisar_por_cpf(exibir_cpf))

        case 6:
            delete_cpf = input("Insira o cpf do cliente a ser deletado: \n")        
            crud.deletar_cliente(delete_cpf)
            print("Cliente deletado!")

        case _:
            print("insira uma opção valida")

    continar_main = input("\nDeseja fazer mais uma operação? (s/n)\n")
    if continar_main.lower() != 's':
        print("Programa terminado.")
        break

# Jorge, 79292297007
# Milton, 32922855007
# Quirino, 19149311069
# Andre, 83754444050