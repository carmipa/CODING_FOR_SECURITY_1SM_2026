# a sinstaxe é molesa

minha_lista_de_compras = ["pão", "leite", "ovos", "café", "açúcar"] # string

# o mais legal? dá para misturar tudo!

dados_malucos = ["Joaão", 30, True, 1.75] # string, int, bool, float

# como acessar os itens?
# é igual string: índice começa em 0

print(minha_lista_de_compras[0]) # pão
print(minha_lista_de_compras[2]) # ovos
print(minha_lista_de_compras[4]) # açúcar

minha_lista_de_compras[0] = "pão integral" # o primeiro item da lista

# lista com -1   
minha_lista_de_compras[-1] = "pão integral" # o ultimo item da lista

# fatiando lista (Slicing)
print(minha_lista_de_compras[1:3]) # ["leite", "ovos"]
print(minha_lista_de_compras[:2]) # ["pão integral", "leite"]
print(minha_lista_de_compras[3:]) # ["café", "pão integral"]

# e para fazer a contagem dos itens da lista?
print(len(minha_lista_de_compras)) # 5


# e para adicionar itens na lista?
minha_lista_de_compras.append("café") # adiciona no final
print(minha_lista_de_compras)

minha_lista_de_compras.insert(1, "café") # adiciona no indice 1
print(minha_lista_de_compras)

minha_lista_de_compras.remove("café") # remove o item "café"
print(minha_lista_de_compras)

minha_lista_de_compras.pop() # remove o ultimo item
print(minha_lista_de_compras)

minha_lista_de_compras.pop(1) # remove o item do indice 1
print(minha_lista_de_compras)