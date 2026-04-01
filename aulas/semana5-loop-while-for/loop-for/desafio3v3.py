numero_tabuada = int(input("Digite um número para ver a tabuada: "))

print(f"--- Tabuada do {numero_tabuada} ---")
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")