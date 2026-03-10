print("--- Utilitário de Enumeração ---")
ip_alvo = input("Digite o IP para iniciar: ")
tecnica = input("Técnica (ex: SYN, UDP, ACK): ")

print("\n[*] Configuração carregada com sucesso")
print(f"[*] Iniciando Scan {tecnica.upper()} no IP {ip_alvo.strip()}...")