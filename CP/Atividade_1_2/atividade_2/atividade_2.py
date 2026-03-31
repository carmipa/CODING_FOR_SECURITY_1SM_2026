from colorama import Fore, Style, init

# Inicializa o colorama para garantir compatibilidade de escape ANSI
init(autoreset=True)

# Definição de cores ANSI 256-bit para maior fidelidade cromática
LARANJA = "\033[38;5;208m"
AMARELO_VIVO = "\033[38;5;226m"

def sistema_soc():
    print(Fore.CYAN + Style.BRIGHT + "\n--- Validade de Níveis de Alerta SOC ---\n")

    print("Escolha o nível de alerta:\n")
    print(Fore.RED + "1 - Vermelho (Crítico)")
    print(LARANJA + "2 - Laranja (Alto)")
    print(AMARELO_VIVO + "3 - Amarelo (Médio)")
    print(Fore.GREEN + "4 - Verde (Baixo)")

    print("\nEstados:")
    print(Fore.MAGENTA + "5 - Crítico")
    print(Fore.BLUE + "6 - Estável")

    # Inputs diretos conforme solicitado
    cor = int(input("\nDigite o número da cor: "))
    estado = int(input("Digite o código do estado: "))

    print("\n" + "=" * 40)

    # Lógica de Alerta baseada em Matriz de Risco
    if cor == 1 and estado == 5:
        print(Style.BRIGHT + Fore.RED + ">>> ALERTA MÁXIMO: Bloquear acessos imediatamente!")

    elif (cor == 1 or cor == 2) and estado == 6:
        print(Style.BRIGHT + LARANJA + ">>> ALERTA ALTO: Iniciar investigação de logs.")

    elif cor == 3 and estado == 6:
        print(Style.BRIGHT + AMARELO_VIVO + ">>> ALERTA MÉDIO: Monitorar tráfego de rede.")

    elif cor == 4:
        print(Style.BRIGHT + Fore.GREEN + ">>> SISTEMA SEGURO: Nenhuma ação necessária.")

    else:
        print(Fore.WHITE + Style.DIM + "[!] Combinação não mapeada ou entrada inválida. [!]")

    print("=" * 40)

sistema_soc()