# Paulo André Carminati
# RM 570877

# CP2 - Coding for Security

# Agenda de Contatos

############################################################################################

agenda = []

menu = """
==================== AGENDA DE CONTATOS ====================

1 - Adicionar Contato
2 - Listar Contatos
3 - Buscar um Contato
4 - Sair

============================================================
"""

try:
    while True:

        print(menu)
        opcao = int(input("Digite uma das opçôes acima de 1 a 4: "))
        print()

        if (opcao == 1):

            adicionar = """
              
            ==================== 1 - Adicionar Contatos ====================
                
            """
            print(adicionar)
            nome =     input("Nome.....: ")
            agenda.append(nome)

            while True:
                try:
                    telefone = int(input("Telefone.: "))
                    agenda.append(telefone)
                    sucesso = """
                    ==================== Contato salvo com sucesso ====================
                    """
                    print(sucesso)
                    input("Aperte qualquer tecla para voltar ao menu principal >>>")
                    break
                except ValueError:
                    erro_telefone = """

                    [!] ==================== O campo telefone aceita apenas números ==================== [!]

                    """
                    print(erro_telefone)

        elif (opcao == 2):
            listar_contatos = f"""      
            ==================== 2 - Listar Contatos ====================
                 
            Lista de contatos Cadastrados: {agenda}     
            """
            print(listar_contatos)
            print()
            input("Aperte qualquer tecla para voltar ao menu principal >>>")
            break

        elif (opcao == 3):
            buscar_contatos = """
                
            ==================== 3 - Buscar Contatos ====================
                
            """
            print(buscar_contatos)
            contato = (input("Digite o nome do contato que deseja pesquisar: "))
            for nome in agenda:
                print(agenda)

        elif (opcao == 4):
            sair = """
            ==================== 4 - Sair ====================
                 
            Sistema Finalisado
                
            """
            break

        else:
            print("[!]  Opção inválida - Digite um número de 1 a 4 [!]")

except ValueError:
    erro1= """
    
        [!] ==================== Erro de digitação! Use apenas números ==================== [!]
        
        """
    print(erro1)

finally:
    print("Programa encerrado com sucesso!")
