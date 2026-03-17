print("-- Auditoria de senhas --")
senha = input("Digite uma senha para auditoria: ")

tamanho = len(senha)

tem_maiuscula = any(caractere.isupper() for caractere in senha)
tem_minuscula = any(caractere.islower() for caractere in senha)

if tamanho >= 8 and tem_maiuscula and tem_minuscula:
    print("\n[+] Senha aprovada nas políticas mínimas de segurança!")
else:
    print("\n[-] Falha na política de senha.")

    if tamanho < 8:
        print("    -> A senha possui menos de 8 caracteres.")

    if not tem_maiuscula:
        print("    -> A senha não possui letra maiúscula.")

    if not tem_minuscula:
        print("    -> A senha não possui letra minúscula.")