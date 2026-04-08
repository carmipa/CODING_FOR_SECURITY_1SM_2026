# sintaxe: usamos chaves {}

aluno = {"nome" : "Paulo","idade" : 46,"curso" : "Direito"}
print(aluno)


aluno = {
    "nome" : "Carlos",
    "idade" : 25,
    "curso" : "Engenhária"
}
print(aluno)

# Acessando e modificando dicionário

print(aluno['nome']) # vai mostrar o valor

# dica de ouro: uso do métido .get() para não tornar erro se a chave não existir
print(aluno.get("cpf", "não informado"))

# e para adicionar ou mudar algo? molesa
aluno["cidade"] = "Sao Paulo" # adicionar uma nova chave
aluno["idade"] = 26 # (atualiza o valor de uma chave que não existe)

# pra remover:
del aluno["idade"]

print(aluno.get("idade", "não informado"))

