# Atividade 2: Conflito de Nomes

## Desafio:

### crie uma variavel global chamada x e dê a ela o valor "global".
### crie uma função que:
    # cria uma variavel local também cahamda x com o valor "local"
    # imprima o valor de x de dentro da função

# chame a funcão

# depois imprima o valor de x de fora da funcão . O que você acha que vai acontecer?

nome = "Paulo"

def meu_nome():
    nome = "Carminati"
    print(f"Ola meu nome é {nome}")

meu_nome()
print(nome)
