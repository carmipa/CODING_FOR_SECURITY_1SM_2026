try:

    print("Calulo da velocidade e distância média:\n")

    distancia = float(input("Digite a distância (m).: "))
    tempo =     float(input("Digite o tempo (s).....: "))

    velocidade_media_ms = distancia / tempo
    velocidade_media_kmh = velocidade_media_ms * 3.6

    print(f"""
    
            O calculo fica da seguinte forma:
            - Distância (m)...............: {distancia}
            - Tempo (s)...................: {tempo}
            - Velocidade média (m/s)......: {velocidade_media_ms}
            - Velocidade média (km/h).....: {velocidade_media_kmh}

    """)

except ValueError:
    print("Erro: Digite apenas números.")

except ZeroDivisionError:
    print("Erro: O tempo não pode ser zero.")




