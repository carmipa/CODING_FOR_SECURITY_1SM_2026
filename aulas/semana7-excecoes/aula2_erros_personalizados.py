# Laçcando seus proprios erros com raise

## e se uma situacao nao for um erro padrâo do python, mas for um erro para a lógica do seu programa?

##  a gente pode lançar um erro de proposito com raise

## por que fazer isso? Para sinalizar que algo inválido aconteceu

## sintaxe:

idade = int(input("Digite sua idade: "))
if idade < 18:
    # lança um erro com uma mensagem nossa!
    raise ValueError("Acesso permitido apenas para maiorres de 18 anos!")
