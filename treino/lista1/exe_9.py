try:

    print("\nCalcula o preço do produto e seu desconto\n")

    preco =    float(input("Digite o preço do produto: "))
    desconto = float(input("digite o desconto produto: "))

    desconto = preco * (desconto / 100)
    preco_final = preco - desconto

    print(f"""" 

        O preço do produto com desconto é de:

        Preço.......: {preco} R$
        Desconto....: {desconto} %
        Preço final.: {preco_final} R$

    """)

except ValueError:
    print("Erro: Digite um número válido.")



    