rm = int(input("Digite o RM com 5 dígitos: "))

d5 = rm % 10
rm = rm // 10

d4 = rm % 10
rm = rm // 10

d3 = rm % 10
rm = rm // 10

d2 = rm % 10
rm = rm // 10

d1 = rm % 10

soma = d1 + d2 + d3 + d4 + d5

print("A soma dos dígitos é:", soma)