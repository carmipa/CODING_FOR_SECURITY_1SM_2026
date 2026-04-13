# Atividade 2 - Coding for Security

**Aluno:** PAULO ANDRÉ CARMINATI — 1TDCPV (RM 570877)
**Prazo de entrega:** 22 de março de 2026 às 23:59

---

## Validador de Níveis de Alerta (SOC)

### 🎯 Objetivo

Aplicar estruturas condicionais complexas (`if`, `elif`, `else`) e operadores lógicos (`and`, `or`) para validação de regras de negócio.

### 📝 Enunciado

Em um Centro de Operações de Segurança (SOC), as cores dos alertas definem a prioridade de atendimento. Crie um sistema que receba a cor do alerta e o estado do sistema (crítico ou estável) para determinar a ação a ser tomada.

### 🚦 Regras de Cores e Lógica

- Se a cor for **"vermelho"** e o estado for **"crítico"**, o programa deve imprimir:
  > `"ALERTA MÁXIMO: Bloquear acessos imediatamente!"`

- Se a cor for **"vermelho"** ou **"laranja"** (mesmo que o estado seja estável), o programa deve imprimir:
  > `"ALERTA ALTO: Iniciar investigação de logs."`

- Se a cor for **"amarelo"** e o estado for **"estável"**, o programa deve imprimir:
  > `"ALERTA MÉDIO: Monitorar tráfego de rede."`

- Para a cor **"verde"**, independente do estado, imprimir:
  > `"SISTEMA SEGURO: Nenhuma ação necessária."`

- Caso o usuário digite qualquer **outra cor**, o programa deve informar:
  > `"Cor inválida: favor reportar ao administrador."`

---

### 💡 Dica

Utilize a função `.lower()` na entrada da cor para evitar erros caso o usuário digite "VERMELHO" ou "Vermelho".
