# tratamento de erros com try...except # Atividade 1: calculadora a prova de balas # Desafio: 

## crie uma calculadora simples que pede dois numeros e uma opraçao (+, -, *, /) 

## Use try/except para garantir que o usuario nao possa dividir por zero(ZeroDivisionError). 

## O programa não quebre se o usuário digitar texto em vez de numeros (ValuesError).except

while True:

    print("""
            Calculadora à prova de erros

            1. Digite o primeiro número
            2. Digite o segundo número
            3. Digite a operação desejada (+, -, *, /, %)
            4. Digite s para sair
    """)

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, /, %): ")

        if operacao == "+":
            soma = num1 + num2
            print(f"""
                Operação escolhida: Adição (+)
                Resultado: {num1} + {num2} = {soma}
                """)

        elif operacao == "-":
            subtracao = num1 - num2
            print(f"""
                Operação escolhida: Subtração (-)
                Resultado: {num1} - {num2} = {subtracao}
                """)

        elif operacao == "*":
            multiplicacao = num1 * num2
            print(f"""
                Operação escolhida: Multiplicação (*)
                Resultado: {num1} * {num2} = {multiplicacao}
                """)

        elif operacao == "/":
            divisao = num1 / num2
            print(f"""
                Operação escolhida: Divisão (/)
                Resultado: {num1} / {num2} = {divisao}
                """)

        elif operacao == "%":
            resto = num1 % num2
            print(f"""
                Operação escolhida: Resto da divisão (%)
                Resultado: {num1} % {num2} = {resto}
                """)

        else:
            print("Operação inválida!")

    except ValueError:
        print("Erro: digite apenas números.")

    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero.")

    sair = input("Digite s para sair ou Enter para continuar: ").lower()
    if sair == "s":
        break