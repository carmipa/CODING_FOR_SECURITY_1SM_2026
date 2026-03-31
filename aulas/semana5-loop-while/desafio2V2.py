porta_atual = 1
soma_portas_pares = 0

print("Inciaiando varredura simulada de portas de rede...\n")

while porta_atual <= 50:

    print(f"Analisando tráfego na porta {porta_atual}...")

    if porta_atual % 2 == 0:
        soma_portas_pares += porta_atual
    porta_atual += 1

print("\n --- varredura concluida ---")
print(f"A soma dos números das portas pares verificada é: {soma_portas_pares}")