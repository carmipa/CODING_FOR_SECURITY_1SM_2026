# Importa a biblioteca 'sys' para interagir com o sistema, usada aqui para encerrar o programa (sys.exit())
import sys
# Importa a biblioteca 'ipaddress' para validar e manipular endereços IP (IPv4 e IPv6)
import ipaddress
# Importa a biblioteca 'os' para interagir com o sistema operacional, usada aqui para limpar a tela do terminal
import os

# Cria uma lista vazia chamada 'ip' que servirá para armazenar os endereços IP suspeitos (em quarentena)
ip = []

# Inicia um loop infinito (True) para manter o programa rodando até que o usuário escolha a opção de sair
while True:
    # Limpa a tela do terminal. "cls" é o comando para limpar tela no Windows. (No Linux/Mac seria "clear")
    os.system("cls")
    
    # Define a string de texto com o menu principal do sistema
    texto = """
    ====================================================================================
    ------------------------------ CENTRO DE OPERÇÕES SOC ------------------------------
    ====================================================================================
    -
    - [1] Adicionar IP Suspeito
    - [2] Listar IPs em Quarentena
    - [3] Remover IP (Falso Positivo)
    - [0] Encerrar Plantão
    -
    - Por favor, selecione uma das opções acima digitando o número correspondente: 
    -
    ====================================================================================
    """

    # Exibe o menu principal na tela
    print(texto)
        
    # Inicia um bloco 'try' para capturar possíveis erros de digitação do usuário (ex: digitar texto em vez de número)
    try:
        # Pede para o usuário digitar a opção e converte a entrada para número inteiro (int)
        opcao = int(input("Opção: "))
        # Limpa a tela após o usuário digitar a opção
        os.system("cls")

        # Verifica se o usuário escolheu a opção 1
        if opcao == 1: # Adicionar IP suspeito a quarentena       
            
            # Inicia um loop interno para manter o usuário na tela de adicionar IP até que a operação tenha sucesso
            while True:
                opcao1 = """

                [+] ---------- Adicionar IP Suspeito a Quarentena ----------[+]      

                """                
                # Exibe o cabeçalho da opção 1
                print(opcao1)
                
                # Pede ao usuário para digitar o IP que deseja adicionar
                ip_quarentena = input("Digite o endereço IP suspeito: ")
                
                # Inicia um bloco 'try' para tratar a entrada de dados e verificar a validade do IP
                try:
                    # Usa a biblioteca 'ipaddress' do Python para validar se o texto digitado é um IP real e correto
                    # Se não for um IP válido, essa linha vai gerar um erro (ValueError) que será capturado pelo 'except' abaixo
                    ipaddress.ip_address(ip_quarentena)                
                    
                    # Se o IP for válido, adiciona o IP na lista 'ip' usando a função .append()
                    ip.append(ip_quarentena) 

                    # Define a mensagem de sucesso
                    sucesso1 = """

                    [+] ---------- IP Suspeito Adicionado com Sucesso ----------[+] 
                                                                        
                    """
                    # Exibe a mensagem de sucesso
                    print(sucesso1)
                    # Pede para o usuário apertar qualquer tecla para continuar (pausa a execução)
                    print("Precione qulquer tecla para voltar ao menu principal!")
                    input()
                    # Limpa a tela
                    os.system("cls") 
                    # Quebra o loop interno e volta ao menu principal, pois a operação foi concluída
                    break    

                # Caso ocorra um erro de valor (ValueError) na validação do IP (linha: ipaddress.ip_address(ip_quarentena))
                except ValueError:
                    # Define a mensagem de erro informando que o IP é inválido
                    erro_validacao_ip = """

                    [x] ------------- Endereço IP Inválido ------------- [x]
                    
                     Por favor, insira um endereço IP válido para continuar.
                     Exemplo: 192.168.1.1
                    
                    [x]------------------------------------------------- [x]

                    """
                    # Exibe a mensagem de erro e o loop recomeça, pedindo o IP novamente
                    print(erro_validacao_ip)
            
        # Verifica se o usuário escolheu a opção 2
        elif opcao == 2: # Listar o ip suspeito da quarentena
            
            # Prepara uma string formatada (f-string) para exibir a lista de IPs que estão guardados na memória
            lista = f"""
                [+] ---------- IPs em Quarentena ----------[+]

                - {ip}

            """ 
            # Exibe a lista na tela
            print(lista)
            # Pede para o usuário apertar qualquer tecla para voltar e limpa a tela (pausa a execução)
            print("Precione qulquer tecla para voltar ao menu principal!")
            input()
            os.system("cls") 
            
        # Verifica se o usuário escolheu a opção 3
        elif opcao == 3: # Remover o ip suspeito da quarentena

            # Inicia um loop interno para a operação de remover IP
            while True:

                opcao3 = """

                [+] ---------- Remover IP Suspeito ----------[+] 

                """
                # Exibe o cabeçalho da opção 3
                print(opcao3)
                
                # Pede para o usuário informar o IP que deseja remover da lista
                ip_quarentena = input("Digite o endereço IP que deseja remover da quarentena: ")

                # Inicia o bloco 'try' para lidar com validações e possíveis erros
                try:                  
    
                    # Trata a entrada de dados e verifica a validade do IP (se foi digitado corretamente)
                    ipaddress.ip_address(ip_quarentena) 
                    
                    # Remove o IP salvo em memória RAM da nossa lista 'ip' usando a função .remove()
                    # Nota: Isso vai gerar um erro ValueError se o IP não estiver na lista!
                    ip.remove(ip_quarentena)

                    # Prepara a mensagem de sucesso usando formatação de string (f-string)
                    sucesso3 = f"""

                        [+] ---------- IP Suspeito {ip_quarentena} Removido da Quarentena com Sucesso ----------[+] 
                                                                            
                        """
                    # Exibe a mensagem de sucesso
                    print(sucesso3)
                    # Pausa para o usuário ler, limpa a tela e quebra o loop (voltando ao menu)
                    print("Precione qualquer tecla para voltar ao menu principal!")
                    input()
                    os.system("cls")
                    break

                # Captura erros tanto da validação do IP (formato incorreto) quanto se o IP não estiver na lista (.remove())
                except ValueError:
                    erro_validacao_ip = """

                        [x] ------------- Endereço IP Inválido ------------- [x]
                        
                        Por favor, insira um endereço IP válido para continuar.
                        Exemplo: 192.168.1.1
                        
                        [x]------------------------------------------------- [x]

                        """
                    # Exibe o erro e o loop se repete
                    print(erro_validacao_ip)
                
        # Verifica se o usuário escolheu a opção 0
        elif opcao == 0:   # encerra o programa
                
            # Define a mensagem de saída
            sair = """
                [x]------------- Encerrar Plantão ------------- [x]
            """
            # Exibe a mensagem
            print(sair)
            # Encerra a execução do script Python de forma limpa
            sys.exit()

        # Caso o usuário digite um número que não seja 1, 2, 3 ou 0
        else:
            # trata opções inválidas de entrada no menu principal
            invalido = """
            [!]------------- Opção inválida ------------- [!]
            
             Por favor escolha uma opçao válida de 1 à 4 (ou 0 para sair)
            
            [!]-------------------------------------------[!]
            
            """
            # Exibe aviso de opção inválida e pausa para que ele possa ler antes de limpar a tela novamente
            print(invalido)
            input("Pressione ENTER para tentar novamente...")   

    # Captura o erro caso o usuário digite letras ou símbolos ao invés de números na seleção do menu (no comando int(input...))
    except ValueError:
        erro1 = """
            [x]------------- Erro de Entrada ------------- [x]
            
             Por favor digite apenas números de 0 a 3   
            
            [x]-------------------------------------------[x]
            
            """
        # Exibe o aviso e pausa a tela
        print(erro1)
        input("Pressione ENTER para tentar novamente...")
