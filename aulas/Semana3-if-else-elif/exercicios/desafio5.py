print("""
    --- SISTEMA DE DETECÇÃO DE WEB APPLICATION FIREWALL (WAF)
""")

payload = input("Digite o PAYLOAD: ")

if(payload == "SELECT" or payload == "</div>"):
# "SELECT" in payload.upper() or "</div>" in payload.upper():
    print("[*] ATAQUE DETECTADO! [*]")
    print(f"{payload}")
else:
    print("Requisição HTTP limpa")
    print(f"{payload}")
