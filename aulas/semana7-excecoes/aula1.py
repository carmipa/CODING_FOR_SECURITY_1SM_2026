# tratamento de erros try except

# Quabrando o código (de propósito!)

## vamos causar algusn erros classicos para ver o que acontece

### 10 / 0 -> opca ZeroDivisionError! Não dá para dividir por zero

### int("abc") -> ValueError na certa! "abc" não é um número

### "2" + 2 -> ih, TypeError! Não dá para somar texto(string) com número(int)

### lista[10] -> IndexError! O índice 10 não existe na lista

# O bloco try... except

## O try...except é como dizer pro pytho

## try (tente): " Ei python, tente executar esse pedaço de código aqui. Pode ser que dê ruim."

## except (se der erro): "Se der algum problema lá no try, em vez de parar tudo, executa esse outro código aqui e segue o baile."

# O bloco try..except

## sintaxe

try:
    # código que pode dar erro
    resultado = 10/0
except:
    #o que fazer se o erro acontecer
    print("Eita, deu um probleminha aqui!")

# Seja Específico no erros

## usar except: sozinho é com um plano B genérico . Pega tudo, mas a gente nunca vai saber o erro em específico

## o ideal é ser específico

try:
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero
    print(f"O resultado é: {resultado}")
except ValueError:
    print("Erro: Voce digitou algo que nao e um numero!")
except ZeroDivisionError:
    print("Erro: Nao da pra dividir por zero!")
