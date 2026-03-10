def escopo():
    porta_incial = int(input("Digite a porta incial para o scan: "))
    porta_final =  int(input("Digite a porta final para o scan.: "))

    total_portas = (porta_final - porta_incial) + 1

    scan = f"""
        Escopo da porta: {porta_incial} até {porta_final}
        Total de portas a serem verificadas: {total_portas} 
    """

    print(scan)

escopo()