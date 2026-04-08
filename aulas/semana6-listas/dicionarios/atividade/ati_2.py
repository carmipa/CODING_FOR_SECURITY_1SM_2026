# Atividade Extra:

# O Desafio: implementar um programa completo em python em dicionário que:

# menu:
# 1 - adicionar tarefa
# 3 - listar tarefas
# 3 - Remover tarefas
# 4 - sair

# Regras:
# 1 - Use um bloco while para manter o programa rodando até o usuário escolher sair
# 2 - use if / elif / else para tratar a escolha do usuário
# 3 - Todas as tarefas devem ser guardadas em um dicionário

# ---------------------------------------------------------------

tarefas = {}
proximo_id = 1

while True:

    menu = """
    
      📂  ----- SISTEMA DE TAREFAS -----  📂
    
      ➕  1 - Adicionar uma tarefa
      📋  2 - Listar tarefas
      🗑️  3 - Remover tarefas
    
      🚪  0 - Sair
    
    ---------------------------------------
    """
    print(menu)

    opcao = input("👉 Digite uma das opções acima: ")
    print()
    

    if (opcao == "1"):

        print("➕ ----- Nova Tarefa ----- ➕")
        print()
        tarefa = input("📝 Digite o nome da tarefa: ")
        tarefas[proximo_id] = tarefa
        proximo_id += 1
        print()
        print(" ✅ Tarefa adicionada com sucesso! ✅")
        print()
        voltar = input("↩️ Digite qualquer tecla para voltar ao menu anterior: ")

    elif (opcao == "2"):

        print("📋 ----- Lista de Tarefas ----- 📋")
        print()
        
        if not tarefas:
            print("📭 Nenhuma tarefa encontrada.")
        else:
            for i in tarefas:
                print(f"🆔 ID: {i} - {tarefas[i]}")

        print()
        voltar = input("↩️ Digite qualquer tecla para voltar ao menu anterior: ")
        

    elif (opcao == "3"):

        print("🗑️ ----- Remover Tarefa ----- 🗑️")
        print()

        if not tarefas:
            print("📭 Nenhuma tarefa para remover.")
        else:
            for i in tarefas:
                print(f"🆔 ID: {i} - {tarefas[i]}")

            print()
            # Usamos o try/except para evitar erro se o usuário digitar letras no ID
            try:
                id_remover = int(input(" 🆔 Digite o ID da tarefa que deseja remover: "))
                
                if id_remover in tarefas:
                    del tarefas[id_remover]
                    print(" ✅ Tarefa removida com sucesso! ✅")
                else:
                    print(" ❌ Tarefa não encontrada! ❌")
            except ValueError:
                print(" ⚠️ Por favor, digite um número de ID válido! ⚠️")
        
        print()
        voltar = input("↩️ Digite qualquer tecla para voltar ao menu anterior: ")
        
        
    elif (opcao == "0"):
        print()
        print(" 🚪 Saindo do programa... Até logo! 🛑")
        print()
        break
    else:
        print("⚠️ Opção inválida! ⚠️")
        print()
        print("👉 Por favor, digite uma opção válida.")
