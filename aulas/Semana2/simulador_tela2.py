from colorama import Fore, init   # Importa recursos de cores do colorama
from datetime import datetime     # Importa a função para pegar data e hora atuais

init(autoreset=True)  # Inicia o colorama e faz a cor voltar ao normal após cada print


# Função para verificar se o IP digitado é válido
def validar_ip(ip):
    partes = ip.split(".")  # Divide o IP em 4 partes usando o ponto como separador

    # Verifica se o IP realmente tem 4 partes
    if len(partes) != 4:
        return False  # Se não tiver 4 partes, o IP é inválido

    try:
        # Tenta converter cada parte do IP para número inteiro
        p1 = int(partes[0])
        p2 = int(partes[1])
        p3 = int(partes[2])
        p4 = int(partes[3])

        # Verifica se cada número está entre 0 e 255
        if 0 <= p1 <= 255 and 0 <= p2 <= 255 and 0 <= p3 <= 255 and 0 <= p4 <= 255:
            return True   # Se todas as partes estiverem corretas, retorna verdadeiro
        else:
            return False  # Se alguma parte estiver fora do intervalo, retorna falso

    except ValueError:
        # Cai aqui se o usuário digitar letras ou símbolos no lugar de números
        return False


# Pega a data atual no formato dia/mês/ano
data = datetime.now().strftime("%d/%m/%Y")

# Pega a hora atual no formato hora:minuto:segundo
hora = datetime.now().strftime("%H:%M:%S")

# Define o nível de severidade fixo como CRÍTICO
nivel_severidade = "CRÍTICO"

print("")  # Apenas pula uma linha na tela


# Laço para pedir o IP de origem até o usuário digitar corretamente
while True:
    ip_origem = input("Digite o IP de origem (999.999.999.999): ")

    # Chama a função para validar o IP digitado
    if validar_ip(ip_origem):
        break  # Se estiver correto, sai do laço
    else:
        # Se estiver errado, mostra mensagem em vermelho e pede novamente
        print(f"{Fore.RED}IP de origem inválido. Digite novamente.\n")


# Laço para pedir o IP de destino até o usuário digitar corretamente
while True:
    ip_destino = input("Digite o IP de destino (999.999.999.999): ")

    # Chama a função para validar o IP digitado
    if validar_ip(ip_destino):
        break  # Se estiver correto, sai do laço
    else:
        # Se estiver errado, mostra mensagem em vermelho e pede novamente
        print(f"{Fore.RED}IP de destino inválido. Digite novamente.\n")


print("")  # Pula uma linha
print("")  # Pula mais uma linha


# Exibe os dados finais formatados na tela
print(f"Data...............: {data}")
print(f"Hora...............: {hora}")
print(f"IP de Origem.......: {ip_origem}")
print(f"IP de Destino......: {ip_destino}")
print(f"Nível de Severidade: {Fore.RED}{nivel_severidade}")