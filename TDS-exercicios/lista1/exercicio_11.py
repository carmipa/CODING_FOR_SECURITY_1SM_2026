salario_antigo = float(input("Digite o valor do salário antes de aumento R$....: "))
salario_novo =   float(input("Digite o valor do salario depois do aumento R$...: "))

aumento = salario_novo - salario_antigo
percentual = (aumento / salario_antigo) * 100

mensagem = f"""

--- Salário de João ---

Salário antigo: R$ {salario_antigo:.2f}
Salário novo:   R$ {salario_novo:.2f}
Aumento:        R$ {aumento:.2f}
Percentual:        {percentual:.2f} %

"""

print(mensagem)