print("-- Scanner de Rede CLI --")
porta_alvo = int(input("Digite a porta encontrada aberta: "))

if (porta_alvo == 2):
    print("\n[!] Atenção: Serviço SSH detectado. Possível vetor de acesso lateral.")

print("\n[*] Varredura concluida")



print(hex(id(int)))