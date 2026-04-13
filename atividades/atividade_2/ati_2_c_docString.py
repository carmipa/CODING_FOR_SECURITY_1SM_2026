tarefas = {}
proximo_id = 1

while True:
    # O menu principal como uma única string formatada
    menu = """
---------------------------------------
      SISTEMA DE TAREFAS
---------------------------------------
1 - ADICIONAR UMA NOVA TAREFA
2 - LISTAR TAREFAS
3 - REMOVER TAREFAS
0 - SAIR

Escolha uma das opcoes acima para acessar
o menu correspondente.
---------------------------------------
"""
    print(menu)

    # Sanitizacao via casting (lembrando que sem try/except deve ser numero)
    opcao = int(input("Digite o numero: "))

    if opcao == 1:
        # Usando aspas triplas para criar o cabecalho da secao
        print("""
--- Nova Tarefa ---
""")
        tarefa = input("Digite o nome da tarefa: ")
        tarefas[proximo_id] = tarefa
        proximo_id += 1

        # Mensagem de sucesso formatada
        print("""
[+] ------------------------------- [+]
    Tarefa adicionada com sucesso!
[+] ------------------------------- [+]
""")
        input("Pressione qualquer tecla para voltar ao menu anterior...")

    elif opcao == 2:
        print("""
--- Lista de Tarefas ---
""")
        if not tarefas:
            print("""
[x] ------------------------------- [x]
    Nenhuma tarefa encontrada!
[x] ------------------------------- [x]
""")
        else:
            # Aqui mantemos o loop para o dicionario
            for i in tarefas:
                print(f"ID: {i} - {tarefas[i]}")

        print("\n")
        input("Pressione qualquer tecla para voltar ao menu anterior...")

    elif opcao == 3:
        print("""
--- Remover Tarefa ---
""")
        if not tarefas:
            print("""
[x] ------------------------------- [x]
    Nenhuma tarefa para remover!
[x] ------------------------------- [x]
""")
        else:
            for i in tarefas:
                print(f"ID: {i} - {tarefas[i]}")

            print("\n")
            id_remover = int(input("Digite o ID da tarefa que deseja remover: "))

            if id_remover in tarefas:
                del tarefas[id_remover]
                print("""
[+] ------------------------------- [+]
    Tarefa removida com sucesso!
[+] ------------------------------- [+]
""")
            else:
                print("""
[x] ------------------------------- [x]
    Tarefa nao encontrada!
[x] ------------------------------- [x]
""")
        input("Pressione qualquer tecla para voltar ao menu anterior...")

    elif opcao == 0:
        print("""
---------------------------------------
Saindo do programa... Ate logo!
---------------------------------------
""")
        break

    else:
        print("""
[!] ------------------------------- [!]
    Por favor, digite uma opcao valida.
[!] ------------------------------- [!]
""")