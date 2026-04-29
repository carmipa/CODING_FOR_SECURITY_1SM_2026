import sys
import ipaddress
import os

ip = []

while True:
    os.system("cls")
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

    print(texto)
        
    try:
        
        opcao = int(input("Opção: "))
        os.system("cls")

        if opcao == 1: # Adicionar IP suspeito a quarentena       
            
            while True:
                opcao1 = """

                [+] ---------- Adicionar IP(s) Suspeito(s) a Quarentena ----------[+]      

                """                
                print(opcao1)
                
                entrada = input("Digite os IPs separados por vírgula (ou '0' para cancelar): ")
                
                if entrada == '0':
                    os.system("cls")
                    break 
                
                lista_novos_ips = entrada.split(",")
                
                adicionados_com_sucesso = 0
                erros_de_validacao = 0
                
                for ip_quarentena in lista_novos_ips:
                    ip_quarentena = ip_quarentena.strip() 
                    
                    try:
                        ipaddress.ip_address(ip_quarentena)                
                        ip.append(ip_quarentena) 
                        adicionados_com_sucesso += 1
                        print(f" [+] IP {ip_quarentena} adicionado à quarentena!")

                    except ValueError:
                        print(f" [x] Erro: O texto '{ip_quarentena}' não é um IP válido e foi ignorado.")
                        erros_de_validacao += 1

                print(f"\n[+] Resumo: {adicionados_com_sucesso} adicionados | {erros_de_validacao} recusados.")
                # Novo loop para validar a entrada com arquitetura segura (Try/Except e Tipagem Estrita)
                while True:
                    try:
                        escolha = int(input("\nDeseja adicionar mais IPs? [1] Continuar | [0] Voltar ao Menu: "))
                        
                        if escolha == 1 or escolha == 0:
                            break # É número e está dentro do limite esperado
                        
                        # Se for número, mas diferente de 1 ou 0
                        print(" [!] Opção errada! Digite apenas o número 1 ou 0.")
                        
                    except ValueError:
                        # Malha fina de segurança: bloqueia tentativas de injetar textos, símbolos ou enters vazios
                        print(" [x] Erro de Segurança! Entradas de texto não são permitidas, digite apenas 1 ou 0.")

                if escolha == 0:
                    os.system("cls")
                    break
                
                os.system("cls") 
                # Se foi '1', ele pula o if do '0', limpa a tela e o loop de adicionar IPs recomeça!
            
        elif opcao == 2: # Listar o ip suspeito da quarentena
            
            lista = f"""
                [+] ---------- IPs em Quarentena ----------[+]

                - {ip}

            """ 
            print(lista)
            print("Precione qulquer tecla para voltar ao menu principal!")
            input()
            os.system("cls") 
            
        elif opcao == 3: # Remover o ip suspeito da quarentena

            while True:

                opcao3 = """

                [+] ---------- Remover IP Suspeito ----------[+] 

                """
                print(opcao3)
                ip_quarentena = input("Digite o endereço IP que deseja remover da quarentena: ")

                try:                  
    
                    # trata a entrada de dados e a validade do ip
                    ipaddress.ip_address(ip_quarentena) 
                    # remove o ip salvo em memoria RAM    
                    ip.remove(ip_quarentena)

                    sucesso3 = f"""

                        [+] ---------- IP Suspeito {ip_quarentena} Removido da Quarentena com Sucesso ----------[+] 
                                                                            
                        """
                    print(sucesso3)
                    print("Precione qualquer tecla para voltar ao menu principal!")
                    input()
                    os.system("cls")
                    break

                except ValueError:
                    erro_validacao_ip = """

                        [x] ------------- Endereço IP Inválido ------------- [x]
                        
                        Por favor, insira um endereço IP válido para continuar.
                        Exemplo: 192.168.1.1
                        
                        [x]------------------------------------------------- [x]

                        """
                    print(erro_validacao_ip)
                
        elif opcao == 0:   # encerra o programa
                
            sair = """
                [x]------------- Encerrar Plantão ------------- [x]
            """
            print(sair)
            sys.exit()

        else:
            # trata opções inválidas de entrada no menu principal
            invalido = """
            [!]------------- Opção inválida ------------- [!]
            
             Por favor escolha uma opçao válida de 1 à 4
            
            [!]-------------------------------------------[!]
            
            """
            print(invalido)
            input("Pressione ENTER para tentar novamente...")   

    except ValueError:
        erro1 = """
            [x]------------- Erro de Entrada ------------- [x]
            
             Por favor digite apenas números de 1 a 4   
            
            [x]-------------------------------------------[x]
            
            """
        print(erro1)
        input("Pressione ENTER para tentar novamente...")
        
        







