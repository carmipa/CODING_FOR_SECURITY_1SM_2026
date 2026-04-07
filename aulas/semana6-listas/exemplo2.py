# percorrer a lista com o for
minha_lista_de_compras = ["pão integral", "leite", "ovos", "café", "pão integral"]

for item in minha_lista_de_compras:
    print(f"Item: {item}")

# percorrer a lista com o for e o index
for i in range(len(minha_lista_de_compras)):
    print(f"Item: {minha_lista_de_compras[i]}")

# percorrer a lista com o for e o index e o valor
for i, item in enumerate(minha_lista_de_compras):
    print(f"Item: {item} na posição {i}")

# percorrer a lista com o for e o index e o valor e o tamanho da lista
for i, item in enumerate(minha_lista_de_compras):
    print(f"Item: {item} na posição {i} de {len(minha_lista_de_compras)}")

# percorrer a lista com o for e o index e o valor e o tamanho da lista e o tamanho do item
for i, item in enumerate(minha_lista_de_compras):
    print(f"Item: {item} na posição {i} de {len(minha_lista_de_compras)} e tamanho {len(item)}")

# percorrer a lista com o for e o index e o valor e o tamanho da lista e o tamanho do item e o tipo do item
for i, item in enumerate(minha_lista_de_compras):
    print(f"Item: {item} na posição {i} de {len(minha_lista_de_compras)} e tamanho {len(item)} e tipo {type(item)}")

# percorrer a lista com o for e o index e o valor e o tamanho da lista e o tamanho do item e o tipo do item e o valor do item
for i, item in enumerate(minha_lista_de_compras):
    print(f"Item: {item} na posição {i} de {len(minha_lista_de_compras)} e tamanho {len(item)} e tipo {type(item)} e valor {item}")