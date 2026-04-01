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

    # 1. PEGAMOS A MOCHILA FORA DO LOOP (INICIALIZAÇÃO)
    total_clientes = 0

    while True:

        opcao = int(input("Digite o número da opção desejada: "))

        if (opcao == 1):
            print("---- Cadastra Cliente ----")
            nome =               input("Nome do cliente...: ")
            ano_nascimento = int(input("Ano de nascimento.:"))

            ano_atual = 2026 - ano_nascimento
            
            # 2. COLOCAMOS MAIS UM NA MOCHILA (INCREMENTO)
            total_clientes = total_clientes + 1

            # 3. EXIBIMOS O QUE TEM NA MOCHILA
            msg_sucesso = f"""

                [+] Cliente Cadastrado com sucesso [+]

                Nome do cliente....: {nome} 
                ano de nascimento..: {ano_nascimento}
                Idade..............: {ano_atual}

                --- Total de clientes nesta sessão: {total_clientes} ---
            """
            print(msg_sucesso)
           
        
        elif (opcao == 2):
            print("---- Executar varredura a partir de arquivo ----")
            
            # Aqui abrimos o arquivo para leitura
            # O Python lê cada linha do arquivo como um item da lista!
            with open("aulas/semana5-loop-while-for/exercicios/alvos.txt", "r") as arquivo:
                bugs_encontrados = 0
                
                # Para cada linha dentro do arquivo...
                for linha in arquivo:
                    ip = linha.strip() # .strip() remove o 'pulo de linha' (\n)
                    print(f"[*] Escaneando IP do arquivo: {ip}...")
                    
                    if ".100" in ip:
                        print(f"    [!] Alvo {ip} vulnerável!")
                        bugs_encontrados += 1
                
                print(f"Varredura de arquivo finalizada. Achados: {bugs_encontrados}")

            
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
            