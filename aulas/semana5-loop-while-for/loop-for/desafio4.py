# Atividade Prática2: Contador de vogais

# 1. Peça ao usuário para digitar uma frase. .lower()
# 2. Crie uma variável contadora para as vogais, inicializada com 0.
# 3. Use um laço for para percorrer cada letra de palavra.
# 4. Se a palavra for um vogal( a, e, i, o, u), incrementar o contador.
# 5. No final, exiba o número total de vogais.

# -------------------------

palavra = input("Digite uma palavra: ").lower()
contador_vogais = 0

for letra in palavra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador_vogais = contador_vogais + 1

print(f"A palavra ´{palavra}´ tem ´{contador_vogais}´ vogais")
