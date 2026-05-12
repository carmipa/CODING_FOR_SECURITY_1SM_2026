#definicao da funcao
def saudacao(nome):
   # criar a mensagem e a retorna
   return f"Ola, {nome}!"

# Chamada da funcao
mensagem_para_maria = saudacao("Maria")
print(mensagem_para_maria) # saida: ola, Maria
print(saudacao("João")) # saida: ola, João