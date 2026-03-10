def bloqueio():

    ip_origem = input("Digite o IP de origem da maquina: ")
    porta_bloqueada = int(input("Digite o número da porta que deseja bloquear: "))
    bloqueio = int(input("Digite o tempo desejado de bloqueio do sistema em H: "))

    tempo_bloqueio = (bloqueio * 60)

    mensagem = f"""
        
        --- Log de bloqueio ---
        
        - IP de origem............: {ip_origem}
        - Porta bloqueada.........: {porta_bloqueada}
        - Tempo de bloqueio (H)...: {bloqueio}
        - Tempo de bloquio em (M).: {tempo_bloqueio}
        
        --- SISTEMA BLOQUEADO ---
        
    """
    print(mensagem)

bloqueio()