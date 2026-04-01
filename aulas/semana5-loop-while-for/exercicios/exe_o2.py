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
            
            # 1. Nossa lista de alvos (a "caixa" de itens)
            alvos = ["192.168.0.1", "10.0.0.5", "172.16.0.100"]
            
            # 2. O contador de vulnerabilidades (FORA do for, igual no desafio das vogais)
            bugs_encontrados = 0
            
            # 3. O for percorrendo os alvos automaticamente
            for ip in alvos:
                print(f"[*] Analisando o IP: {ip}...")
                
                # Vamos fingir que o IP final .100 tem uma falha
                if ".100" in ip:
                    print(f"    [!] VULNERABILIDADE DETECTADA EM {ip}!")
                    bugs_encontrados = bugs_encontrados + 1 # Incrementando o contador manual
            
            # 4. Resultado final (depois que o for acaba)
            print("-" * 30)
            print(f"Varredura concluída! Total de falhas: {bugs_encontrados}")

            
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
            