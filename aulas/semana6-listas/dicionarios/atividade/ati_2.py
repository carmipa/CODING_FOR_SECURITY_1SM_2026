# Atividade Extra:
import os
from platform import system

# O Desafio: implementar um programa completo em python que:
# menu:
# 1 - adicionar tarefa
# 3 - listar tarefas
# 3 - Remover tarefas
# 4 - sair

# Regras:
# 1 - Use um bloco while para manter o programa rodando até o usuário escolher sair
# 2 - use if / elif / else para tratar a escolha do usuário
# 3 - Todas as tarefas devem ser guardadas em uma lista

# ---------------------------------------------------------------

menu = """
    
    ----- SISTEMA DE TAREFAS -----
    
    1 - Adicionar uma tarefa
    2 - Listar tarefas
    3 - Remover tarefas
    4 - Sair
    
    -------------------------------

"""

# Criando o dicionário vazio e um ID antes de entrar no laço
dicionario_tarefas = {}
id_tarefa = 1

while True:
    # O menu precisa aparecer e receber a opção AQUI DENTRO para o sistema perguntar de novo
    print(menu)
    opcao = int(input("Digite uma das opções acima: "))

    if (opcao == 1):

        add_tareda = input("Digite o nome da tarefa desejada: ")

        # A sintaxe de dicionário usa dois pontos (:) e estamos adicionando ao invés de recriá-lo
        dicionario_tarefas[id_tarefa] = add_tareda
        id_tarefa += 1

        print("Tarefa adicionada com sucesso!")
        print(dicionario_tarefas)
        
        # Pausa para digitar 0 e voltar ao inicio do while
        voltar = input("\nDigite 0 para voltar ao menu inicial! ")
        while voltar != '0':
            voltar = input("Opção inválida. Digite 0 para exibir o menu inicial: ")
        
    elif (opcao == 2):

        print("Listar Tarefas")
        print()
        print(dicionario_tarefas)
    
    elif (opcao == 3):

        print("Remover Tarefas")
        print(({tarefa}))
    
    elif (opcao == 4):
        print("Sair")
        break




    

    




