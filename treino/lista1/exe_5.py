try:
    num1 = int(input("Digite o primeiro número X.: "))
    num2 = int(input("Digite o segundo número Y..: "))

    potencia = num1 ** num2

    print(f"""
    
        O Resultado de X({num1}) elevado a Y({num2}) é igual a {potencia}.
    
    """)

except ValueError:
    print("\n\n\tErro: Por favor, digite apenas números inteiros.")


