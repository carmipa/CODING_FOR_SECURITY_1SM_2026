numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

maior = numero1
if numero2 > maior:
    maior = numero2

while True:
    if maior % numero1 == 0 and maior % numero2 == 0:
        print(f"O MMC entre {numero1} e {numero2} é {maior}")
        break
    maior += 1