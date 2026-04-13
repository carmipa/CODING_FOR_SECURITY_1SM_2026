tarefas = {}
proximo_id = 1

while True:
    print("""
---------------------------------------
      SISTEMA DE TAREFAS
---------------------------------------
1 - ADICIONAR UMA NOVA TAREFA
2 - LISTAR TAREFAS
3 - REMOVER TAREFAS
0 - SAIR
---------------------------------------
""")

    try:
        # Primeiro ponto de falha: conversao para int
        opcao = int(input("Digite o numero da opcao: "))

        if opcao == 1:
            print("\n--- Nova Tarefa ---")
            tarefa = input("Digite a descricao: ")
            tarefas[proximo_id] = tarefa
            proximo_id += 1
            print("\n[+] Sucesso: Tarefa registrada.")
            input("\nPressione Enter para continuar...")

        elif opcao == 2:
            print("\n--- Lista de Tarefas ---")
            if not tarefas:
                print("\n[x] Dicionario vazio.")
            else:
                for i in tarefas:
                    print(f"ID: {i} | Tarefa: {tarefas[i]}")
            input("\nPressione Enter para continuar...")

        elif opcao == 3:
            print("\n--- Remover Tarefa ---")
            if not tarefas:
                print("\n[x] Nao ha tarefas para remover.")
            else:
                for i in tarefas:
                    print(f"ID: {i} | Tarefa: {tarefas[i]}")

                # Segundo ponto de falha: conversao do ID para int
                id_remover = int(input("\nDigite o ID para remover: "))

                if id_remover in tarefas:
                    del tarefas[id_remover]
                    print("\n[+] Sucesso: Item deletado.")
                else:
                    print("\n[x] Erro: ID inexistente.")
            input("\nPressione Enter para continuar...")

        elif opcao == 0:
            print("\nEncerrando o sistema...")
            break

        else:
            print("\n[!] Opcao invalida. Escolha entre 0 e 3.")

    except ValueError:
        # Captura erros de conversao (letras no lugar de numeros)
        print("""
***************************************
   ERRO: Entrada invalida!
   Por favor, digite apenas numeros.
***************************************
""")
        input("Pressione Enter para tentar novamente...")