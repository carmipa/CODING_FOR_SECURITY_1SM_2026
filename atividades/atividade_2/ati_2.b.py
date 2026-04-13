tarefas = {}
proximo_id = 1

while True:
    menu = """

        ---------------------------------------

        ----- SISTEMAA DE TAREFAS -----

        1 - ADICIONAR UMA NOVA TAREFA
        2 - LISTAR TAREFAS
        3 - REMOVER TAREFAS

        0 - SAIR 

        obs: Escolha uma das opçoes acima para acessar o menu correspondente

        ---------------------------------------

    """

    print(menu)
    opcao = int(input("Digite um dos números para acessar o menu respectivo: "))

    if (opcao == 1):

        print("----- Nova Tarefa -----")
        print()
        print()
        tarefa = input("Digite o nome da tarefa: ")
        tarefas[proximo_id] = tarefa
        proximo_id += 1
        print()
        print("[+] ----- Tarefa adicionada com sucesso! ----- [+]")
        print()
        print()
        print()
        voltar = input("↩️ Digite qualquer tecla para voltar ao menu anterior: ")

    if (opcao == 2):

        print("----- Lista de Tarefas -----")

        if not tarefas:
            print()
            print()
            print()
            print(" [x] ----- Nenhuma tarefa encontrada! ----- [x]")
        else:
            for i in tarefas:
                print(f"ID: {i} - {tarefas[i]}")
        print()
        print()
        print()
        voltar = input("↩️ Digite qualquer tecla para voltar ao menu anterior: ")

    if (opcao == 3):

        print("----- Remover Tarefa -----")
        print()
        print()

        if not tarefas:
            print(" [x] ----- Nenhuma tarefa para remover! ----- [x]")
        else:
            for i in tarefas:
                print(f"ID: {i} - {tarefas[i]}")

            print()
            print()
            print()

            id_remover = int(input("Digite o ID da tarefa que deseja remover: "))

            if id_remover in tarefas:
                del tarefas[id_remover]
                print()
                print()
                print()
                print("[+] ----- Tarefa removida com sucesso! ----- [+]")
            else:
                print()
                print()
                print()
                print(" [x] ----- Tarefa não encontrada! ----- [x]")

    print()
    print()
    print()
    voltar = input("↩️ Digite qualquer tecla para voltar ao menu anterior: ")

    if (opcao == "0"):
        print()
        print()
        print()
        print("Saindo do programa... Até logo!")
        break
    else:
        print()
        print()
        print()
        print("Por favor, digite uma opção válida.")



