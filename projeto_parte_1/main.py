from crud import Crud

crud = Crud()

resposta = int(input("Escolha uma operação para realizar:\n"
                 '(1) criar um cliente;\n'
                 '(2) atualizar um cliente;\n'
                 '(3) listar todos os clientes;\n'
                 '(4) pesquisar cliente por nome;\n'
                 '(5) exibir cliente por cpf;\n'
                 '(6) deletar um cliente;\n'))

match resposta:  
    case 1:
        ccpf = input("Insira o cpf: \n")
        cnome = input("Insira o nome: \n")
        cemail = input("Insira o email: \n")
        ctelefone = input("Insira o telefone: \n")
        cdata_nascimento = input("Insira a data_nascimento: \n")
        cnacionalidade = input("Insira a nacionalidade: \n")
        cestado_civil = input("Insira o estado_civil: \n")
        crenda_mensal = input("Insira a renda_menal: \n")
        clogradouro = input("Insira o logradouro: \n")
        cbairro = input("Insira o bairro: \n")
        ccidade = input("Insira o cidade: \n")
        cestado = input("Insira o estado: \n")
        ccep = input("Insira o cep: \n")
        data_entrada=""
        
        crud.criar_cliente(ccpf, cnome, cemail, ctelefone, cdata_nascimento, cnacionalidade, 
                       cestado_civil, crenda_mensal, clogradouro, cbairro, ccidade, 
                        cestado, ccep, data_entrada)
        print("Cliente criado!")

    case 2:
        """atualizar_cliente(self, cpf, nome, email, telefone, data_nascimento, nacionalidade, estado_civil, 
                    renda_mensal, logradouro, bairro, cidade, estado, cep): """
        cpf = input("Insira o cpf de quem será alterado:")
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
            "12- cep\n"))
            match campo:
                case 1:
                    campo_alterado = input("Digite o novo nome:")
                    nome = campo_alterado
                case 2:
                    campo_alterado = input("Digite o novo email:")
                    email = campo_alterado
                case 3:
                    campo_alterado = input("Digite o novo telefone:")
                    telefone = campo_alterado
                case 4:
                    campo_alterado = input("Digite a nova data de nascimento:")
                    data_nascimento = campo_alterado
                case 5:
                    campo_alterado = input("Digite a nova nacionalidade:")
                    nacionalidade = campo_alterado
                case 6:
                    campo_alterado = input("Digite o novo estado civil:")
                    estado_civil = campo_alterado
                case 7:
                    campo_alterado = float(input("Digite a nova renda mensal:"))
                    renda_mensal = campo_alterado
                case 8:
                    campo_alterado = input("Digite o novo logradouro:")
                    logradouro = campo_alterado
                case 9:
                    campo_alterado = input("Digite o novo bairro:")
                    bairro = campo_alterado
                case 10:
                    campo_alterado = input("Digite a nova cidade:")
                    cidade = campo_alterado
                case 11:
                    campo_alterado = input("Digite o novo estado:")
                    estado = campo_alterado
                case 12:
                    campo_alterado = input("Digite o novo cep:")
                    cep = campo_alterado
                case _:
                    print("Opção inválida.")
                    
            continuar = input("Deseja alterar outro campo? (s/n)")
            #Como está sendo alterado um campo por vez, esse break é utilizado quando não se deseja atualizar nenhum outro campo
            if continuar.lower() != 's':
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

# Quirino, 19149311069
# Andre, 83754444050