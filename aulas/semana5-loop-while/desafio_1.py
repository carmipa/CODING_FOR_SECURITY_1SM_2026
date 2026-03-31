# Variável acumuladora do custo total
custo_total = 0.0

# Lê a primeira despesa antes do loop
despesa = float(input("Digite o valor da primeira despesa: "))

# Continua enquanto o valor digitado for diferente de 0
while (despesa != 0):

    # Soma a despesa ao custo total
    custo_total = custo_total + despesa

    # Pede a próxima despesa
    despesa = float(input("Digite o valor da próxima despesa: "))

# Exibe o resultado final formatado
print(f"Custo total do projeto: R$ {custo_total}")

