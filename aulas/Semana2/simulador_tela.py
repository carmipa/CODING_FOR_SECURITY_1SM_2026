# importa a biblioteca de cores
from colorama import Fore, init

# importa as bibliotecas de data e hora
from datetime import datetime
init(autoreset=True)

#criacao de variavies e inputs de entrada de dados
data = datetime.now().strftime("%d/%m/%Y")
print("")
hora = datetime.now().strftime("%H:%M:%S")
ip_origem = input("Digite o IP de origem: (999.999.999.999): ")
ip_destino = input("Digite o IP de destino: (999.999.999.999): ")
nivel_severidade = "CRÍTICO"

# pula 2 linhas
print("")
print("")

# impreme o resultado dos inputs
print(f"Data...............: {data}")
print(f"Hora...............: {hora}")
print(f"IP de Origem.......: {ip_origem}")
print(f"IP de Destino......: {ip_destino}")

# imprime o input com a cor vermelha
print(f"Nível de Severidade: {Fore.RED}{nivel_severidade}")

