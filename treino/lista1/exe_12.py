# O RM de um aluno da FIAP é composto por 5 dígitos. Sua tarefa é escrever um algoritmo que
# recebe um RM e retorna a somatória de todos os dígitos do RM. Por exemplo, suponha que
# o aluno tenha o RM 56395, seu algoritmo deverá imprimir como saída 28 = 5+6+3+9+5.
# Dica: realize várias divisões e restos de divisões por 10.

print("--- Calculadora de RM ---\n")

try:
    rm = int(input("Digite o seu RM: "))

    print(f"RM: {rm}")

    rm1 = int(input("Digite o primeiro dígito do seu RM.: "))
    rm2 = int(input("Digite o segundo dígito do seu RM..: "))
    rm3 = int(input("Digite o terceiro dígito do seu RM.: "))
    rm4 = int(input("Digite o quarto dígito do seu RM...: "))
    rm5 = int(input("Digite o quinto dígito do seu RM...: "))
    rm6 = int(input("Digite o sexto dígito do seu RM....: "))

    print(f"A somatória dos dígitos do seu RM é: {rm1 + rm2 + rm3 + rm4 + rm5 + rm6}")

except ValueError:
    print("Erro: Digite apenas números inteiros.")