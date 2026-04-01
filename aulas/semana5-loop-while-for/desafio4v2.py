palavra = input("Digite uma palavra: ").lower()
contador = 0

for letra in palavra:
    if letra in "aeiou":
        contador += 1

print(contador)
