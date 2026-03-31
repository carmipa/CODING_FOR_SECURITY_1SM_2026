print("--- CALCULADORA DE RISCO CVSS ---")

score = float(input("Digite o Score CVSS da vulnerabilidade (0.0 a 10.0): "))

if (score >= 9.0):
    print("[CRÍTICO] Correção exigida!")
elif (score >= 7.0):
    print("[ALTO] Agendar patch para a próxima janela.")
elif (score >= 4.0):
    print("[MÉDIO] Monitorar e corrigir no próximo ciclo")
else:
    print("[BAIXO] Risco aceitável ou baixo impacto.")



