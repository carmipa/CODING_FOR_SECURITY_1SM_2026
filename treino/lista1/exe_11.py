from decimal import DivisionByZero
from decimal import Decimal

print("--- Calculadora de Percentual de Aumento Salarial ---\n")

try:
    # Continuamos usando a regra de ouro do replace pro uso brasileiro com Decimal!
    salario_antes =  Decimal(input("Digite o salário antigo (R$)..: "))
    salario_depois =  Decimal(input("Digite o salário novo (R$)...: "))

    if (salario_antes <= 0):
        print("Erro: O salário base para calcular o aumento precisa ser maior que zero.")
    
    elif (salario_depois < salario_antes):
        print("Erro: O salário novo não pode ser menor que o salário antigo.")

    else:
        aumento = (salario_depois - salario_antes)
        percentual = (aumento / salario_antes) * 100
        print(f"""O aumento do salário foi de:

                  - Salario original.......: {salario_antes} R$
                  - Salário após o aumento.: {salario_depois} R$
                  - percentual de aumento..: {percentual} %
        """)

except Exception:
    print("Erro: Valores inválidos. Digite os salários apenas com números.")
except DivisionByZero:
    print("Erro: O salário base para calcular o aumento precisa ser maior que zero.")
        