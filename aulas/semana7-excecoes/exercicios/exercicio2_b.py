nomes = ["Ana", "Bia", "Carlos"]

try:
    indice = int(input(f"Digite um índice entre 0 e {len(nomes)-1}: "))
    print(f"O nome no índice {indice} é: {nomes[indice]}")

except IndexError:
    print(f"Erro: Esse índice não existe! Por favor, escolha um número entre 0 e {len(nomes)-1}.")
except ValueError:
    print("Erro: Você precisa digitar um número inteiro.")