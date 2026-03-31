soma =0
numero = int(input("Digite um numero (O para sair): "))
while numero != 0:
    soma += numero
    numero = int(input("Digite outro número(0 para sair): "))
print (f"O valor final é {soma}")