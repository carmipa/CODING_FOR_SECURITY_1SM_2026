falha = "SQL Injection"
cvss = int(input("Digite uma valor entre 0 e 10: "))
patch = input("Patche existir digite True ou False: ")

escala = (cvss *10 ) /10

print(f"Nome da Falha detectada: {falha.upper().strip()}")
print(f"Valor atual do ataque: {escala}")
print(f"Existe um patch de correção: {patch}")
