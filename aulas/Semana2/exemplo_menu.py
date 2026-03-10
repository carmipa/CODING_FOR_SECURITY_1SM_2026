while True:
    # menu de cadastro
    print("****** PORTO SEGURO - OFICINAS ******")
    print("Escolha uma das opções abaixo:")
    print("1 - Cadastro")
    print("2 - Cadastro do Veiculo")
    print("3 - Descrição do Problema")
    print("4 - Agendar Oficina")
    print("5 - Orçamento e pagamento")
    print("6 - Pagamento")
    print("7 - Indicar uma Oficina para convênio")
    print("0 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    # Nessa opção é possível fazer o cadastro de um novo usuário/cliente ou pesquisar por um usuário existente
    if (opcao == 1):

        while True:
            print("CADASTRO")
            print("1 - Pesquisar usuário")
            print("2 - Novo usuário")
            print("0 - Menu princípal")
            opcao = int(input("Digite a opção desejada: "))

            if (opcao == 1):
                # faz a pesquisa se o usuário existe ou não no sistema
                while True:
                    # usuário cadastrado para teste:
                    # 1
                    # 2
                    # 3

                    cli1 = 1
                    cli2 = 2
                    cli3 = 3

                    codigo = int(input("Digite o código do usuário: "))

                    if (codigo == cli1 or codigo == cli2 or codigo == cli3):
                        print("Usuário já cadastrado! Você já pode ir para o agendamento!")
                        break
                    elif (codigo != cli1 or codigo != cli2 or codigo != cli3):
                        print("Usuário não está cadastrado! Faça o seu cadastro!")
                        break
                    else:
                        break

            # faz o cadastro do cliente e salva automáticamente
            elif (opcao == 2):
                print("CADASTRAR NOVO CLIENTE")
                print("Dados do Cliente:")
                cpf = int(input("Digite o CPF ou CNPJ(apenas números).........: "))
                nome = input("Digiter o nome...............................: ")
                dataNascimento = int(input("Digite a data de nascimento (apenas números).: "))
                print("Endereço do cliente:")
                logradouro = input("Digite o logradouro..........................: ")
                numero = int(input("Digite o número (apenas números).............: "))
                cep = int(input("Digite o CEP (apenas números)................: "))
                print("\n")
                print("************ Cliente cadastrado com sucesso! ************")
                print("\n")

            # testa as opções do menu
            elif (opcao != 1 or opcao != 2 or opcao != 0):
                print("Opção inválida! Digite a opção correta!")

            # quando escolhe o "0" volta ao menu princípal do ssistema
            elif (opcao == 0):
                break
            break


    elif (opcao == 2):
        print("CADASTRO DO VEICULO")
        fabricante = input("Fabricante do veiculo: ")
        modelo = input("Modelo do veiculo: ")
        anoFabricacao = int("Ano de fabricação do veiculo: ")

    elif (opcao == 3):
        print("DESCRIÇÃO DO PROBLEMA")
        print(
            "Descreva o problema que está ocorrendo no seu veiculo e se possível e você tiver conhecimento de mecánica aponte onde ocorre o problema")
        descricaoProblema = input("Descrição do problema: ")
        aponteProblema = input("Local do problema: ")

    elif (opcao == 4):

        while True:
            print("AGENDAR AFICINA")
            dataAgendamento = int(input("Digite a data (apenas números): "))
            print("Escolha o horário de atendimento:")
            print("1 - Manha")
            print("2 - tarde")

    elif (opcao != 1 or opcao != 2 or opcao != 3 or opcao != 4 or opcao != 5 or opcao != 6 or opcao != 7 or opcao != 0):
        print("Opção inválida!")
        print("Digite a opção correta!")
