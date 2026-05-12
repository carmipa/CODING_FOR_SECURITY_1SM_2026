import subprocess

print("--- Coletor de Informações de Rede ---")

resultado = subprocess.run(["ipconfig", "-all"], capture_output=True, text=True)
saida_texto = resultado.stdout

# Exibe a saída do comando na tela (os dados que você sentiu falta)
print(saida_texto)

# Usamos .upper() para garantir que encontre "IPV4" mesmo que o Windows escreva "IPv4"
if "IPV4" in saida_texto.upper():
    print("[+] Adaptador de rede IPv4 detectado.")
else:
    print("[-] Nenhum endereço IPv4 encontrado.")