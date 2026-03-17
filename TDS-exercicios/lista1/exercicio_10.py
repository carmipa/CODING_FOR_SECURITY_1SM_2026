# Solicita a distância em metros do usuário
distancia = float(input("Digite a distancia percorrida em metros (m): "))
# Solicita o tempo em segundos do usuário
tempo = float(input("Digite o tempo percorrido em segundos (s):"))

# Calcula a velocidade em metros por segundo (m/s)
velocidade_ms = distancia / tempo
# Converte a velocidade de m/s para km/h
velocidade_kmh = velocidade_ms * 3.6

# Exibe os resultados formatados com duas casas decimais
print(f"A velocidade média é de {velocidade_ms:.2f} m/s.")
print(f"A velocidade média é de {velocidade_kmh:.2f} km/h.")
