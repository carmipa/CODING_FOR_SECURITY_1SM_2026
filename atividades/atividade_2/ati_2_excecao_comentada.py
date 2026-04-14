tarefas = {}  # Inicializa um dicionário vazio para armazenar as tarefas (ID: Descrição)
proximo_id = 1  # Contador para gerar IDs automáticos e sequenciais para as tarefas

while True:  # Inicia um laço infinito (simulando o 'do while') para manter o menu rodando
    # Exibe o menu visual para o usuário
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

    try:  # Tenta executar o bloco abaixo; se ocorrer um erro de tipo, o 'except' captura
        # Solicita a opção e tenta converter para número inteiro (int)
        # Se o usuário digitar uma letra, o erro ValueError será gerado aqui
        opcao = int(input("Digite o numero da opcao: "))

        if opcao == 1:  # Caso o usuário escolha adicionar
            print("\n--- Nova Tarefa ---")
            tarefa = input("Digite a descricao: ")  # Recebe o texto da tarefa
            tarefas[proximo_id] = tarefa  # Adiciona ao dicionário usando o ID atual como chave
            proximo_id += 1  # Incrementa o contador para a próxima tarefa
            print("\n[+] Sucesso: Tarefa registrada.")
            input("\nPressione Enter para continuar...")

        elif opcao == 2:  # Caso o usuário escolha listar
            print("\n--- Lista de Tarefas ---")
            if not tarefas:  # Verifica se o dicionário 'tarefas' está vazio
                print("\n[x] Dicionario vazio.")
            else:
                # Percorre todas as chaves (IDs) dentro do dicionário
                for i in tarefas:
                    print(f"ID: {i} | Tarefa: {tarefas[i]}")
            input("\nPressione Enter para continuar...")

        elif opcao == 3:  # Caso o usuário escolha remover
            print("\n--- Remover Tarefa ---")
            if not tarefas:  # Verifica se existe algo para remover
                print("\n[x] Nao ha tarefas para remover.")
            else:
                # Mostra a lista atual para o usuário saber qual ID escolher
                for i in tarefas:
                    print(f"ID: {i} | Tarefa: {tarefas[i]}")

                # Tenta converter o ID digitado para inteiro
                # Se digitar letra aqui, também cai no ValueError lá embaixo
                id_remover = int(input("\nDigite o ID para remover: "))

                if id_remover in tarefas:  # Verifica se o ID existe nas chaves do dicionário
                    del tarefas[id_remover]  # Remove a entrada correspondente ao ID
                    print("\n[+] Sucesso: Item deletado.")
                else:
                    print("\n[x] Erro: ID inexistente.")
            input("\nPressione Enter para continuar...")

        elif opcao == 0:  # Caso o usuário queira sair
            print("\nEncerrando o sistema...")
            break  # Sai do laço 'while True', encerrando o programa

        else:  # Caso digite um número que não está no menu
            print("\n[!] Opcao invalida. Escolha entre 0 e 3.")

    except ValueError:
        # Este bloco é executado SE o int(input(...)) falhar (ex: digitar "abc")
        print("""
***************************************
   ERRO: Entrada invalida!
   Por favor, digite apenas numeros.
***************************************
""")
        input("Pressione Enter para tentar novamente...")