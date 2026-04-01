palavra = input("Digite uma palavra: ").lower()

contador_vogais = (
    palavra.count("a") +
    palavra.count("e") +
    palavra.count("i") +
    palavra.count("o") +
    palavra.count("u")
)

print(f"O número total de vogais é {contador_vogais}")