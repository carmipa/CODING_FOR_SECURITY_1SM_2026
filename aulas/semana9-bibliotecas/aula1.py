import subprocess
import platform

print("--- Teste de conectividade ---")
alvo = "8.8.8.8"
print(f"[*] Dispara ping contra o alvo: {alvo}")

# O comando é passado como uma lista de strings ' -c4' no linux ou '-n 4' no windows 
# vamos usar '-c 1' / '-n 1' para ser rapido. adapte dependendo dos pcs do laboratório
comando = ["ping", "-n", "1", alvo]

resultado = subprocess.run(comando, capture_output=True, text=True)
print(resultado.returncode)
if resultado.returncode == 0:
    print("[+] Host está UP (online!)")
else:
    print("[-] Host está DOWN (offline)")

print(resultado.stdout)
