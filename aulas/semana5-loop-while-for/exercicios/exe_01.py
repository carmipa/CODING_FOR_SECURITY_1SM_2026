def exemplo():

    mensagem = """
        --- SISTEMA DE GERENCIAMENTO ---
    """

    menu = """Esconlha um das opções abaixo para executar uma função:

    1 - Cadastra Cliente
    2 - Excecutar varredura de vulnerabilidades
    3 - Calcular risco
    4 - Sair

    """

    print(mensagem)
    print(menu)

    while True:

        opcao = int(input("Digite o número da opção desejada: "))

        if (opcao == 1):
            print("---- Cadastra Cliente ----")
            nome =               input("Nome do cliente...: ")
            ano_nascimento = int(input("Ano de nascimento.:"))

            ano_atual = 2026 - ano_nascimento

            cadastra_client = f"""

                [+] Cliente Cadastrado com sucesso [+]

                Nome do cliente....: {nome} 
                ano de nascimento..: {ano_nascimento}
                Idade..............: {ano_atual}

            """
            print(cadastra_client)
        
        elif (opcao == 2):
            print("---- Executar varredura de vulnerabilidades ----")
            print("Varredura concluida com sucesso!")
            
        elif (opcao == 3):
            print("--- Calcular Risco ----")
            valor1 = float(input("Digite o valor 1: "))
            valor2 = float(input("Digite o valor 2: "))
            
            porcentagem = (valor1 / valor2) * 100
            
            print(f"A porcentagem do risco atual é de: {porcentagem}")
        
        elif (opcao == 4):
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida!")

exemplo()
            