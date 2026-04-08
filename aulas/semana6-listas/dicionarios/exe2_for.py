# percorrendo um dicionário
#
# tem várias formas de usar o for com o dicionário
#
# 1 pegando só chave
#
# for chave in aluno:
#
# 2 pegando so os valore
#
# for valor in aluno.values():
#
# 3 pegando os dois (o mmelhor jeito!):
#
# for chave, valor in aluno. item():
# print(f"{chave} : {valor}")

# imprime todos os nomes das chaves
dados_pessoais = {"Nome" : "Paulo André Carminati",
                  "Idade" : 46,
                  "Cidade" : "Guarulhos"
                  }

for chave in dados_pessoais:
    print(chave)

print()

# imprime e retorna os valores das chaves
dados_pessoais = {"Nome" : "Paulo André Carminati",
                  "Idade" : 46,
                  "Cidade" : "Guarulhos"
                  }

for chave in dados_pessoais.values():
    print(chave)

print()
# imprme os valore da chave e valor

dados_pessoais = {"Nome" : "Paulo André Carminati",
                  "Idade" : 46,
                  "Cidade" : "Guarulhos"
                  }

for chave in dados_pessoais.items():
    print(chave)