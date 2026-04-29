# "Desenvolva um programa em Python que simule um sistema de verificação de permissões de acesso.
# O programa deve solicitar que o usuário digite o seu nível de acesso. O seu programa deve ser
# imune a variações de letras maiúsculas ou minúsculas (ex: "Admin", "ADMIN" ou "admin" devem ser
# tratados da mesma forma). Com base na entrada, utilize estruturas condicionais para exibir a mensagem
# correspondente conforme as regras abaixo:

# Se o nível for "admin", imprimir: [+] Permissão Total Concedida. Acesso a todos os sistemas.

# Se o nível for "dev" ou "developer", imprimir: [*] Permissão de Desenvolvedor. Acesso aos projetos e repositórios.

# Se o nível for "user", "aluno" ou "professor", imprimir: [ ] Permissão de Usuário Padrão. Acesso apenas ao sistema básico.

# Para qualquer outro valor, imprimir: [-] Nível de acesso desconhecido. Permissões negadas."

def sistema_de_acessso():

    mensagem = """

        * ---------- SISTEMA DE VERIFICAÇÃO DE ACESSOS ---------- *

    ...................................................................

        Nível de acesso de usuários ao sistem:

        1 - admin
        2 - dev
        3 - developer
        3 - user
        4 - aluno
        5 - professor

    ...................................................................
    
    """
    print(mensagem)

    print("\n")
    opcao = int(input("Digite um dos números acima para acessar o sistema: "))
    print("\n")

    if (opcao == 1):
        print("[*] Permissão total concedida! Acesso a todos os sistemas [+]")
    elif (opcao == 2 or opcao == 3):
        print("[+] Permissão de sesenvolvedor. Acesso aos projetos e repositórios [+]")
    elif (opcao == 3 or opcao == 4 or opcao == 5):
        print("[+] Permissão de Usuário Padrão. Acesso apenas ao sistema básico [+]")
    else:
        print("...................................................................\n")
        print("   [-] Nível de acesso desconhecido. Permissões negadas. [-]\n")
        print("...................................................................")

sistema_de_acessso()

