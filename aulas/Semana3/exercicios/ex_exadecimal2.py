print("-- Conversor para Hexadecimal --")

numero = int(input("Digite um número decimal: "))

print("Decimal.....:", numero)
print("Hex com 0x..:", hex(numero))
print("Hex sem 0x..:", format(numero, "x"))
print("Hex maiúsc..:", format(numero, "X"))
