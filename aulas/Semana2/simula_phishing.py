def Phishing():
    nome = input("Digite seu nome: ")
    departamento = input("Digite o departamento a que pertence o funcionário: ")
    email = input("Digite seu E-mail: ")

    mensagem = f"""
        ⚠️ Dados do usuário comprometidos ⚠️
        🆔 nome.........: {nome}
        🏢 departamento.: {departamento}
        📧 email........ds: {email.lower()}

        ⚠️ ---- DADOS COMPROMETIDOS --- ⚠️
    """

    print(mensagem)

Phishing()
