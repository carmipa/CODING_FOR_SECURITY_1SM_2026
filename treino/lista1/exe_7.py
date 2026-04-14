try:

    numero = int(input("Digite um número inteiro entre 0 e 99: "))

    if (0 <= numero <= 99):

        desena = numero // 10
        unidade = numero % 10

        print(f"""
                O número......: {numero} é composto de:
                desenas.......: {desena}  
                e unidades....: {unidade} 
        """)

    else:
        print("O número deve estar entre 0 e 99!")

except ValueError:
    print("Erro: Digite um número inteiro válido!")

