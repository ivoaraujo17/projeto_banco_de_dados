from crud import Crud

crud = Crud()
while True:
    print("\nMenu de operações:\n"
                    '(1) criar um cliente;\n'
                    '(2) atualizar um cliente;\n'
                    '(3) listar todos os clientes;\n'
                    '(4) pesquisar cliente por nome;\n'
                    '(5) exibir cliente por cpf;\n'
                    '(6) deletar um cliente;\n'
                    '(7) sair do programa\n')
    resposta = int(input("Digite o número correspondente à operação desejada: "))

    match resposta:  
        case 1:
            
            ccpf = crud.validar_cpf(input("Insira o cpf: "))
            while not ccpf[0]:
                ccpf = crud.validar_cpf(input("Cpf inválido. Insira o cpf: "))

            cnome = crud.validar_nome(input("Insira o nome: "))
            while not cnome[0]:
                cnome = crud.validar_nome(input("Nome inválido. Insira o nome: "))

            cemail = crud.validar_email(input("Insira o email: "))
            while not cemail[0]:
                cemail = crud.validar_email(input("Email inválido. Insira o email: "))

            ctelefone = crud.validar_telefone(input("Insira o telefone: "))
            while not ctelefone[0]:
                ctelefone = crud.validar_telefone(input("Telefone inválido. Insira o telefone: "))

            cdata_nascimento = crud.validar_data_nascimento(input("Insira a data de nascimento: "))
            while not cdata_nascimento[0]:
                cdata_nascimento = crud.validar_data_nascimento(input("Data de nascimento inválida. Insira a data de nascimento: "))

            cnacionalidade = crud.validar_nacionalidade(input("Insira a nacionalidade: "))
            while not cnacionalidade[0]:
                cnacionalidade = crud.validar_nacionalidade(input("Nacionalidade inválida. Insira a nacionalidade: "))

            cestado_civil = crud.validar_estado_civil(input("Insira o estado civil: "))
            while not cestado_civil[0]:
                cestado_civil = crud.validar_estado_civil(input("Estado civil inválido. Insira o estado civil: "))

            crenda_mensal = crud.validar_renda_mensal(input("Insira a renda mensal: "))
            while not crenda_mensal[0]:
                crenda_mensal = crud.validar_renda_mensal(input("Renda mensal inválida. Insira a renda mensal: "))

            clogradouro = crud.validar_logradouro(input("Insira o logradouro: "))
            while not clogradouro[0]:
                clogradouro = crud.validar_logradouro(input("Logradouro inválido. Insira o logradouro: "))

            cbairro = crud.validar_bairro(input("Insira o bairro: "))
            while not cbairro[0]:
                cbairro = crud.validar_bairro(input("Bairro inválido. Insira o bairro: "))

            ccidade = crud.validar_cidade(input("Insira a cidade: "))
            while not ccidade[0]:
                ccidade = crud.validar_cidade(input("Cidade inválida. Insira a cidade: "))

            cestado = crud.validar_estado(input("Insira o estado: "))
            while not cestado:
                cestado = crud.validar_estado(input("Estado inválido. Insira o estado: "))

            ccep = crud.validar_cep(input("Insira o CEP: "))
            while not ccep[0]:
                ccep = crud.validar_cep(input("CEP inválido. Insira o CEP: "))

            
            result = crud.criar_cliente(ccpf[1], cnome[1], cemail[1], ctelefone[1], cdata_nascimento[1], cnacionalidade[1], 
                        cestado_civil[1], crenda_mensal[1], clogradouro[1], cbairro[1], ccidade[1], 
                            cestado[1], ccep[1])
            print(result)

        case 2:
            
            procurando_cpf = crud.pesquisar_por_cpf(input("\nInsira o cpf de quem será alterado: "))
            while not procurando_cpf[0]:
                procurando_cpf = crud.pesquisar_por_cpf(input("CPF invalido. Insira o cpf de quem será alterado: "))
            
            cpf = procurando_cpf[1][0][0]
            nome= [True, ""]
            email= [True, ""]
            telefone= [True, ""]
            data_nascimento= [True, ""]
            nacionalidade= [True, ""]
            estado_civil= [True, ""]
            renda_mensal= [True, ""]
            logradouro= [True, ""]
            bairro= [True, ""]
            cidade= [True, ""]
            estado= [True, ""]
            cep= [True, ""]
            while True:
                print("\nMenu de operações:\n"
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
                "13- salvar alterações e sair\n")
                campo = int(input("Digite o número correspondente ao campo que deve ser atualizado: "))
                match campo:
                    case 1:
                        campo_alterado = crud.validar_nome(input("Insira o novo nome: "))
                        while not campo_alterado[0]:
                            campo_alterado = crud.validar_nome(input("Nome inválido. Insira novamente o nome: "))
                        nome = campo_alterado
                    case 2:
                        campo_alterado = crud.validar_email(input("Insira o novo email: "))
                        while not campo_alterado[0]:
                            campo_alterado = crud.validar_email(input("Email inválido. Insira novamente o email: "))
                        email = campo_alterado
                    case 3:
                        campo_alterado = crud.validar_email(input("Digite o novo telefone:"))
                        while not campo_alterado[0]:
                            campo_alterado = crud.validar_telefone(input("Telefone inválido. Insira novamente o telefone: "))
                        telefone = campo_alterado
                    case 4:
                        campo_alterado = crud.validar_data_nascimento(input("Digite a nova data de nascimento:"))
                        while not campo_alterado[0]:
                            campo_alterado = crud.validar_data_nascimento(input("Data inválida. Insira novamente a data de nascimento: "))
                        data_nascimento = campo_alterado
                    case 5:
                        campo_alterado = crud.validar_nacionalidade(input("Digite a nova nacionalidade:"))
                        while not campo_alterado[0]:
                            campo_alterado = crud.validar_nacionalidade(input("Nacionalidade inválida. Insira novamente a nacionalidade: "))
                        nacionalidade = campo_alterado
                    case 6:
                        campo_alterado = crud.validar_estado_civil(input("Digite o novo estado civil:"))
                        while not campo_alterado[0]:
                            campo_alterado = crud.validar_estado_civil(input("Estado civil inválido. Insira novamente o estado civil: "))
                        estado_civil = campo_alterado
                    case 7:
                        campo_alterado = crud.validar_renda_mensal(input("Digite a nova renda mensal:"))
                        while not campo_alterado[0]:
                            campo_alterado = crud.validar_renda_mensal(input("Renda mensal inválida. Insira novamente a renda mensal: "))
                        renda_mensal = campo_alterado
                    case 8:
                        campo_alterado = crud.validar_logradouro(input("Digite o novo logradouro:"))
                        while not campo_alterado[0]:
                            campo_alterado = crud.validar_logradouro(input("Logradouro inválido. Insira novamente o logradouro: "))
                        logradouro = campo_alterado
                    case 9:
                        campo_alterado = crud.validar_bairro(input("Digite o novo bairro:"))
                        while not campo_alterado[0]:
                            campo_alterado = crud.validar_bairro(input("Bairro inválido. Insira novamente o bairro: "))
                        bairro = campo_alterado
                    case 10:
                        campo_alterado = crud.validar_cidade(input("Digite a nova cidade:"))
                        while not campo_alterado[0]:
                            campo_alterado = crud.validar_cidade(input("Cidade inválida. Insira novamente a cidade: "))
                        cidade = campo_alterado
                    case 11:
                        campo_alterado = crud.validar_estado(input("Digite o novo estado:"))
                        while not campo_alterado[0]:
                            campo_alterado = crud.validar_estado(input("Estado inválido. Insira novamente o estado: "))
                        estado = campo_alterado
                    case 12:
                        campo_alterado = crud.validar_cep(input("Digite o novo cep:"))
                        while not campo_alterado[0]:
                            campo_alterado = crud.validar_cep(input("CEP inválido. Insira novamente o cep: "))
                        cep = campo_alterado
                    case 13:
                        result = crud.atualizar_cliente(cpf, nome[1], email[1], telefone[1], data_nascimento[1], nacionalidade[1], 
                                                        estado_civil[1], renda_mensal[1], logradouro[1], bairro[1], cidade[1], 
                                                        estado[1], cep[1])
                        print(result[1])
                        break
                    case _:
                        print("Opção inválida.")
                        
                """continuar_atualizar = input("Deseja alterar outro campo? (s/n)")
                #Como está sendo alterado um campo por vez, esse break é utilizado quando não se deseja atualizar nenhum outro campo
                if continuar_atualizar.lower() != 's':
                    crud.atualizar_cliente(cpf, nome, email, telefone, data_nascimento, nacionalidade, estado_civil, 
                            renda_mensal, logradouro, bairro, cidade, estado, cep)
                    print("Cliente atualizado!")
                    break"""
                    
        case 3:
            print(crud.listar_todos_clientes()[1])

        case 4:
            pesquisa_nome = input("Insira o nome para ser pesquisado: ")
            print(crud.pesquisar_por_nome(pesquisa_nome)[1])

        case 5:
            exibir_cpf = input("Insira o cpf para ser ser exibido: ")
            print(crud.pesquisar_por_cpf(exibir_cpf)[1])

        case 6:
            delete_cpf = input("Insira o cpf do cliente a ser deletado: ")        
            crud.deletar_cliente(delete_cpf)
            print("Cliente deletado!")

        case 7:
            print("Programa finalizado.")
            break

        case _:
            print("insira uma opção valida")


# Jorge, 79292297007
# Milton, 32922855007
# Quirino, 19149311069
# Andre, 83754444050