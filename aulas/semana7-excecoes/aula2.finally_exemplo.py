# Criando um arquivo de teste para você executar e observar
def demonstrar_finally(simular_erro):
    print(f"\n--- Teste com erro = {simular_erro} ---")
    try:
        print("1. Abrindo arquivo...")
        if simular_erro:
            resultado = 10 / 0
        else:
            resultado = 10 / 2
        print(f"2. Operação realizada. Resultado: {resultado}")
    except ZeroDivisionError:
        print("3. Tratei o erro de divisão!")
    finally:
        print("4. FECHANDO ARQUIVO (Sempre rodando!)")

demonstrar_finally(False) # Fluxo normal
demonstrar_finally(True)  # Fluxo com erro
