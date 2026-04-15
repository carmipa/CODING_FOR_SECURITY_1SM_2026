# Atividade prática 1: Cálculadora Revisitada

## Pegue a calculadora da aula anterior

## modifique-a para:

### lançcar um valueError com raise se a operção digitada não for '+', '-', '*' ou '/'

### usar um else para mostrar o resultado, garantindo que ele só apareça se o cálculo der certo

### Usar um finally para imprimir uma mensagem "Fim da operção" no final, independentemente do que aconteceu.

# -----------------------------------------------------------------------------------------------------------------------------

while True:

    print("""
    
        Calculadora Revisada

        1 = soma
        2 = subtração
        3 = multiplicação
        4 = divisão

        0 = sair

        ---------------------------------------------
    """)

    try:
        escolha = input("Digite uma opção: ")

        if escolha == "0":
            print("Saindo da calculadora...")
            break

        elif escolha != "1" and escolha != "2" and escolha != "3" and escolha != "4":
            raise ValueError("Opção inválida! Digite apenas 1, 2, 3, 4 ou 0.")

        num1 = float(input("Digite o primeiro número.......: "))
        num2 = float(input("Digite o segundo número........: "))

        if escolha == "1":
            resultado = num1 + num2
            operacao = "+"

        elif escolha == "2":
            resultado = num1 - num2
            operacao = "-"

        elif escolha == "3":
            resultado = num1 * num2
            operacao = "*"

        elif escolha == "4":
            resultado = num1 / num2
            operacao = "/"

    except ValueError as e:
        print(f"Erro: {e}")

    except ZeroDivisionError:
        print("Erro! Divisão por zero não é permitida.")

    else:
        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")

    finally:
        print("Fim da operação.\n")