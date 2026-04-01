# Peça ao usuário para digitar um número inteiro.

# Use um laço for e a função range() par exibir a tabuada desse número, do 1 ao 10.

numero = int(input("Digite um número para saber sua tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


