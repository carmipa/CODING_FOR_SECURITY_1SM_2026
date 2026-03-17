from colorama import Fore, Style, init

init(autoreset=True)

def texte_firewall():
    texto = """
       [!] Simulação de Bloqueio de Firewall [1]
    """

    print(texto)

    ip = input("Digite o número do IP: ")

    if ip == "192.168.1.50":
        texto_ip1 = """
            IP Correto!
        """
        print(texto_ip1)
    else:
        texto_ip2 = """
            IP Incorreto!

            [!] Acesso Bloqueado [!]
        """
        print(Fore.RED + texto_ip2 + Style.RESET_ALL)


texte_firewall()