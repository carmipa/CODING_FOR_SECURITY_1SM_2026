produto = input("Digite o nome do produto: ")
preco = float(input("Preço do produto: "))
percentual = float(input("Digite o percentual de desconto: "))

desconto = preco * (percentual / 100)
novo_preco = preco - desconto

print("Produto: ", produto)
print("Preço: ", preco)
print("Percentual de desconto: ", percentual, "%")
print("Desconto: ", desconto)
print("Novo preço: ", novo_preco)