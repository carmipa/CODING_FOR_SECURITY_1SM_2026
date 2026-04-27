# A clausula finally: aconteça o que acontecer

## O bloco finally é teimoso: ele sempre executa no final.abs
## não importa se deu erro ou não, se teve except ou else, o finally roda igual.

# Sintaxe:

try:
    print("1. Abrindo um recursso...")
    # forçando um erro a acontecer
    resultaado = 10/0
    print("isso nunca será impresso")
except ZeroDivisionError:
    print("2. Ops! Ocorreu um erro durante a operação.")
finally:
    # Este bloco é executado mesmo que tenha ocorrido um erro
    print("3. Limpando tudo! O recurso foi fechado. (Bloco finally  )")