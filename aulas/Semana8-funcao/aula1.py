# Anatomia de uma função!

## A gente usa a palavra def(de definir) para criar uma função

### Palavra-chave def e o nome da função

### Parametros dentro dos parenteses

#### def calcular_area(largura, altura):

#### 3. corpo da funcao (o que ela faz)

#### 4. palavra-chave 'return' para devolver a resposta

##### return resultado

###############################################################################################

# Anatomia de uma funcao
## chamando a funcão: Agora é só usar!

def calcular_area(largura, altura):

    resultado = largura * altura

    area_retangulo_1 = calcular_area(10,5)
    area_retangulo_2 = calcular_area(7,3)

    print(area_retangulo_1) # saida: 50
    print(area_retangulo_2) # saida: 21

    return resultado

calcular_area()

####################################################################################################

# Paramentros e arguntmentos

## é so o nome , mas é bom saber a difrença

## parametros
### são variáveis que a gente define na criação da função . são com as etiquetas das entradas
### def calcular_area(largura, altura): -> largura e altura são paramentros

## argumentos:
## São os valores

####################################################################################################

# escopo de variaveis: onde ela existe?

## escopo local: uma variável criada dentro de uma funcao só existe e pode ser usada ali dentro, e como um segredo daquela função

def minha_funcao():
    variavel_local = "Segredo"
    print(variavel_local)

minha_funcao() # funciona!
# print(variavel_local) # vai dar erro! 


#####################################################################################################

# Escopo global: onde ela existe?

# Escopo global`uma variavel criada fora de qualquer funcao existe em todo script

variavel_global = "Estou em todo lugar"

def mostrar_global():
    print(variavel_global)

mostrar_global() # funciona!