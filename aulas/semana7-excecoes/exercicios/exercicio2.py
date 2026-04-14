# Atrividade prática 2: Acessando L:istas

## Desafio:

### Crie uma lista, por exemplo: nomes = ["Ana", "Bia", "Carlos"]

### Peça ao usuário para digitar um índicce e mostre o nome correspondente.nonlocal

### Use try...except IndexError para tratar o caso de uim índiuce que não existe (ex: índice 10)

# --------------------------------------------------------------


nomes = []

while True:
    print("""

    [*] ----- ACESSANDO LISTAS ----- [*]

    1. Adicionar nome
    2. Buscar nome por índice
    3. Sair

    """)

    try:
        opcao = input("Digite uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            nomes.append(nome)

        elif opcao == "2":
            indice = int(input("Digite o índice: "))

            try:
                print(f"O nome no índice {indice} é: {nomes[indice]}")
            except IndexError:
                print("Índice inválido")

        elif opcao == "3":
            print("[x] ----- SAINDO DA APLICAÇÃO ----- [x]")
            break

        else:
            print("Opção inválida")

    except ValueError:
        print("Digite um número válido para o índice.")