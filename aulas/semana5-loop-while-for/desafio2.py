porta_atual = 1
soma_portas_pares = 0

while True:
    if (porta_atual <= 50):
        print(f"Porta: {porta_atual}")
        if porta_atual % 2 == 0:
            soma_portas_pares += porta_atual

        porta_atual += 1
    else:
        break
print(f"Soma de todas as portas: {soma_portas_pares}")

