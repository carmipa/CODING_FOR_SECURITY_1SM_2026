# Atiuvidade 1 - pratica
# crie uma lista (to-do-list) com duas tarefas iniciais (ex: ["lavar a louça", "estudar python"])
# adicionar uma nova tarefa no final da alista: "Passear com o cachorro".
# remover a primeira tarefa da lista("lavar a louça").
#imprima a lista final de tarefas para ver como ficou

lista_tarefas = ["lavar a louça", "Estudar Python"]
print(lista_tarefas)
print(f"Lista de tarefas inicial: {lista_tarefas}")

lista_tarefas.append("Passear com o cachorro")
print(lista_tarefas)
print(f"Lista de tarefas após adicionar uma tarefa: {lista_tarefas}")

lista_tarefas.remove("lavar a louça")
print(lista_tarefas)
print(f"Lista de tarefas após remover uma tarefa: {lista_tarefas}")





