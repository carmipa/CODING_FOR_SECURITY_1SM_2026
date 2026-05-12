# Atividade prática 1: saudação

## Desafio:

### - Crie uma função chamada saudação.
### - Ela deve receber um nome como parametro
### - A função deve retornar um String no formato "Ola, [nome]!"
### - Depois, chame a função com o seu nome e imprima o resultado

#####################################################################################################

def saudacao(nome="Paulo André", sobrenome="Carminati"):
    # Valores padrão permitem chamar saudacao() sem passar nada na chamada
    return f"Ola meu nome é {nome} e meu sobrenome é {sobrenome}"

# Chamamos a função dentro do print (o retorno vai direto para a tela)
print(saudacao())

###########################################################

# Argumentos: imutaveis vs.mutaveis

## tipos imutaveis (numeros, strings, tuplas): a função recebe uma copia. Se ela alterar o valor. a variável orginal, de for, não muda.

def tentar_mudar(numero):
    numero = 100 # isso só muada a cópia local
    print(f"Dentro da função: {numero}")

valor = 5
tentar_mudar(meu_numero)
print(f"Fora da função: {meu_numero}") # continua 5

###########################################################


