## Atividade Prática pré CP: Resiliência em Sistemas de Segurança (Tratamento de Exceções)

**Contextualização:** Você foi recém-contratado para atuar no Centro de Operações de Segurança (SOC) de uma grande empresa. A equipe utiliza um script em Python desenvolvido internamente para gerenciar rapidamente uma lista de endereços IP suspeitos (uma "quarentena"). Esse painel via linha de comando permite que os analistas adicionem novos IPs identificados em alertas, listem os bloqueios atuais e removam IPs que, após análise, provaram ser falsos positivos.

**O Problema:** O sistema funciona bem na teoria, mas falha na prática. Durante o tratamento de incidentes, os analistas precisam agir muito rápido e, frequentemente, cometem erros de digitação. O menu do painel exige que o usuário digite um número inteiro (1 a 4) para escolher uma opção. Se o analista esbarrar em uma letra (por exemplo, "w") ou apertar **Enter** sem digitar nada, o programa tenta converter essa entrada inválida, sofre um **crash** (fechando inesperadamente com um erro do tipo `ValueError`) e apaga toda a lista de IPs que estava armazenada na memória.

**Sua Missão:** Seu gestor enviou o arquivo base do script para você e pediu que você blinde o código contra essas falhas de digitação, utilizando os conceitos de tratamento de erros e exceções em Python.

### Requisitos Técnicos

1. **Identifique o ponto de falha:** Localize no código base a linha onde a entrada do usuário está sendo convertida para um número inteiro.
2. **Implemente o `try...except`:** Envolva a captura da opção do menu em um bloco de tratamento de erros especificamente para capturar falhas de valor (`ValueError`).
3. **Mantenha a execução (Resiliência):** Caso o usuário digite um caractere inválido (letras, símbolos ou deixe em branco), o programa **não pode quebrar**. Ele deve interceptar o erro, exibir uma mensagem de alerta clara (ex: `"[!] Erro de entrada: Por favor, digite apenas números para navegar no menu."`) e reiniciar o loop, exibindo o menu novamente sem perder os dados da lista de IPs.
4. **Preserve as funcionalidades:** As lógicas de inserir, consultar, remover IPs e encerrar o plantão devem continuar funcionando exatamente como no código original.

### Exemplo de Saída Esperada (Simulando o erro de digitação)

1. Adicionar IP suspeito
2. Listar IPs em quarentena
3. Remover IP (Falso Positivo)
4. Encerrar Plantão

**Por favor, selecione uma das opções:** `admin`  
`[!] Erro de entrada: Por favor, digite apenas números para navegar no menu.`

1. Adicionar IP suspeito
2. Listar IPs em quarentena...
