while True:

    try:
        print()
        num1 = int(input("Digite o primeiro número inteiro.: "))
        num2 = int(input("Digite o segundo número inteiro..: "))
        print()

        soma = num1 + num2
        subtracao = num1 - num2
        multiplicacao = num1 * num2
        divisao = num1 / num2
        resto = num1 % num2
        divisao_exata = num1 // num2

        print(f"""
            
            O Resultado das operações é o seguinte:

            soma............ = {num1} +  {num2} = {soma}
            subtracao....... = {num1} -  {num2} = {subtracao}
            multiplicação... = {num1} *  {num2} = {multiplicacao}
            divisao......... = {num1} /  {num2} = {divisao}
            resto........... = {num1} %  {num2} = {resto}
            divisao_exata... = {num1} // {num2} = {divisao_exata}

        """)
    except ValueError:
        print("\n[x] Erro! Digite apenas números inteiros. [x]\n")
    except ZeroDivisionError:
        print("\n[x] Erro! Não é possível dividir por zero. [x]\n")