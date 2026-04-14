while True:
    print("""

    Calculadora Complexa:

    1 - Soma (+)
    2 - Subtração (-)
    3 - Multiplicação (*)
    4 - Divisão (/)
    5 - Resto da divisão (%)
    6 - Divisão Exata (//)

    0 = sair

    """)

    try:

        opcao = int(input("Digite uma das opções acima para ver o resultado desejado: "))

        if (opcao == 1):
            num1 = int(input("Digite o primeiro número.: "))
            num2 = int(input("Digite o segundo número..: "))
            print(f"O resultado da operação de soma é..: {num1} + {num2} = {num1 + num2}")
            print("\n")
            input("Pressione Enter para voltar ao menu principal")

        elif (opcao == 2):
            num1 = int(input("Digite o primeiro número....: "))
            num2 = int(input("Digite o segundo número.....: "))
            print(f"O resultado da operação de subtração é.: {num1} - {num2} = {num1 - num2}")
            print("\n")
            input("Pressione Enter para voltar ao menu principal")

        elif (opcao == 3):
            num1 = int(input("Digite o primeiro número.........: "))
            num2 = int(input("Digite o segundo número..........: "))
            print(f"O resultado da operação de multiplicação é.: {num1} * {num2} = {num1 * num2}")
            print("\n")
            input("Pressione Enter para voltar ao menu principal")

        elif (opcao == 4):
            num1 = int(input("Digite o primeiro número...: "))
            num2 = int(input("Digite o segundo número....: "))
            print(f"O resultado da operação de divisão é.: {num1} / {num2} = {num1 / num2}")
            print("\n")
            input("Pressione Enter para voltar ao menu principal")

        elif (opcao == 5):
            num1 = int(input("Digite o primeiro número............: "))
            num2 = int(input("Digite o segundo número.............: "))
            print(f"O resultado da operação de resto da divisão é.: {num1} % {num2} = {num1 % num2}")
            print("\n")
            input("Pressione Enter para voltar ao menu principal")

        elif (opcao == 6):
            num1 = int(input("Digite o primeiro número.........: "))
            num2 = int(input("Digite o segundo número..........: "))
            print(f"O resultado da operação de divisão exata é.: {num1} // {num2} = {num1 // num2}")
            print("\n")
            input("Pressione Enter para voltar ao menu principal")

        elif (opcao == 0):
                print("Saindo...")
                break

        else:
            print("Opção inválida!")
    
    except ValueError:
        print("\n")
        print("[x] Erro: Digite um números inteiros! [x]")
        print("\n")
    except ZeroDivisionError:
        print("\n")
        print("[x] Erro: Divisão por zero! [x]")
        print("\n")
