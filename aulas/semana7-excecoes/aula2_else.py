# usar cláusula ELSE para rodar um código só se tudo der certo try.

# conhecer o finally: o bloco que roda de qualquer jeito!

# aprender a lançar nossos próprios erros com o RAISE

# ------------------------------------------------------------------------------

# A clausula else: O código do "Deu certo"

## o else no try... except é um bonus: ele só executa se o bloco try terminar sem nenhum erro.abs

## é perfeito para colcoar o código que depende do sucesso da operação

# Sintaxe:

try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Entrada inválida!")
else:
    # só roda se o try funcionou
    print(f"Você digitou o número {numero}. Sucesso!")

# ------------------------------------------------------------------------------

