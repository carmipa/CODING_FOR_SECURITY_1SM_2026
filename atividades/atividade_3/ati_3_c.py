import sys
import ipaddress
import os

ips_em_quarentena = {} # Dicionário: { "IP": "Motivo" }

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

                [+] ---------- Adicionar IP Suspeito a Quarentena ----------[+]      

                """                
                print(opcao1)
                ip_quarentena = input("Digite o endereço IP suspeito: ")
                
                # trata a entrada de dados e a validade do ip
                try:
                    # usa a biblioteca do python para validadar se o ip digitado esta correto!
                    ipaddress.ip_address(ip_quarentena)
                    
                    motivo = input("Digite o motivo (ex: Port Scan, Malware): ")
                    ips_em_quarentena[ip_quarentena] = motivo 

                    sucesso1 = """

                    [+] ---------- IP Suspeito Adicionado com Sucesso ----------[+] 
                                                                        
                    """
                    print(sucesso1)
                    print("Precione qulquer tecla para voltar ao menu principal!")
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
            
        elif opcao == 2: # Listar o ip suspeito da quarentena
            
            print("\n                [+] ---------- IPs em Quarentena ----------[+]")
            if len(ips_em_quarentena) == 0:
                print("\n                - Nenhum IP em quarentena no momento.")
            else:
                for endereco, motivo in ips_em_quarentena.items():
                    print(f"                - IP: {endereco} | Motivo: {motivo}")
            print("\n                [+] ---------------------------------------[+]\n")
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
                    
                    if ip_quarentena in ips_em_quarentena:
                        del ips_em_quarentena[ip_quarentena]
                        sucesso3 = f"""

                        [+] ---------- IP Suspeito {ip_quarentena} Removido da Quarentena com Sucesso ----------[+] 
                                                                            
                        """
                        print(sucesso3)
                    else:
                        print(f"\n                        [!] O IP {ip_quarentena} não foi encontrado na lista de quarentena!\n")
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
        
        







