custo_total = 0.0

despesa = float(input("Digite o valor da primeira despesa: "))

while True:
    if (despesa != 0):
        custo_total += despesa
        despesa = float(input("Digite o valor da próxima despesa: "))
    else:
        break

print(f"Custo total do projeto: R$ {custo_total:.2f}")