print("---SIEM: Analisador de logs ---")
hora_acesso = int(input("Digite a hora de acesso (0 - 23): "))
usuario = input("Digite o nome do usuário: ")

if (hora_acesso >= 0 and hora_acesso <= 5) and usuario == "root":
    print("[ALERTA] Possível comprometimento! Acesso root fora do horário comercial.")
else:
    print("[*} Log de acesso normal registrado.")