try:

    print("""

    Guarda Roupas

    Digite a quantidade de: 
    - camisas
    - calças
    - pares de sapatos

    """)

    camisas = int(input("Quantidade de camisas...........: "))
    calcas =  int(input("Quantidade de calças............: "))
    sapatos = int(input("Quantidades de pares de sapatos.: "))

    total = camisas * calcas * sapatos

    print(f"""
    
        Guarda Roupas:
        camisas..........: {camisas}
        calças...........: {calcas}
        Pares de sapatos.: {sapatos}

        Total de combinações possíveis: {total}

    """)

except ValueError:
    print("Erro: Digite apenas números inteiros.")