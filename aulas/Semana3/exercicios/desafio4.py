print("--- CALCULO DE NOTAS")
nome = input("Digite seu nome: ")
nota = float(input("Digite a nota do aluno (0.0 a 10.0): "))

if (nota >= 9.0):
    print(f"Exelente! (A)")
    print(f" Nome do aluno: {nome}")
    print(f" Nota do aluno: {nota}")
elif (nota == 8.9):
    print(f"Bom (B)!")
    print(f" Nome do aluno: {nome}")
    print(f" Nota do aluno: {nota}")
elif (nota  >= 7.0):
    print(f"BOM!")
    print(f" Nome do aluno: {nome}")
    print(f" Nota do aluno: {nota}")
elif (nota == 6.9):
    print(f"Regular! (C)")
    print(f" Nome do aluno: {nome}")
    print(f" Nota do aluno: {nota}")
elif (nota >=5.0):
    print(f"Regular! (C)")
    print(f" Nome do aluno: {nome}")
    print(f" Nota do aluno: {nota}")
elif (nota <= 4.9):
    print(f"nsuficiente! (D)")
    print(f" Nome do aluno: {nome}")
    print(f" Nota do aluno: {nota}")
else:
    print(f"Insuficiente! (D)!")
    print(f" Nome do aluno: {nome}")
    print(f" Nota do aluno: {nota}")