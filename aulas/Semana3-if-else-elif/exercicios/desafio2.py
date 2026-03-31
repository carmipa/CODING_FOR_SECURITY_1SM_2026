from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)

def login():
    mensagem = """
        --- Login de Usuário ---
    """

    print(mensagem)

    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha do usuário: ")

    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if usuario == "admin":
        if senha == "12345":
            print(Fore.GREEN + "\n[+] Acesso Concedido" + Style.RESET_ALL)
            print(f"[LOG] Usuário: {usuario} | Data/Hora: {data_hora}")
        else:
            texto_erro = "\n[!] Acesso Negado\n"
            texto_erro += "    -> Senha incorreta para o usuário admin.\n"
            texto_erro += f"\n[LOG] Usuário: {usuario} | Data/Hora: {data_hora}"

            print(Fore.RED + texto_erro + Style.RESET_ALL)
    else:
        texto_erro = "\n[!] Acesso Negado\n"
        texto_erro += "    -> Usuário não é administrador.\n"
        texto_erro += f"\n[LOG] Usuário: {usuario} | Data/Hora: {data_hora}"

        print(Fore.RED + texto_erro + Style.RESET_ALL)

login()