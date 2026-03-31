print("-- Auditoria de senhas --")
senha = input("Digite uma senha para auditoria: ")

# A função len() conta a quantidade de caracteres da string
tamanho = len(senha)

if (tamanho >= 8):
    print("\n[+] Senha aprovada nas políticas de tamanho minímo! .")
else:
    print("\n[-] Falha: A senha possui menos de 8 caracteres e é vulnerável a força-bruta")
