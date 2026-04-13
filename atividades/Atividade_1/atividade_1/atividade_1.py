def processador_cadastro():
    boas_vindas = """"
    
    -- # PROCESSADOR DE DADOS DE CADASTRO # -- 
    
    """""
    print(boas_vindas)

    primeiro_nome =      input("Digite o primeiro nome..............: ")
    sobrenome =          input("Digite o sobrenome..................: ")
    ano_nascimento = int(input("Digite seu ano de nascimento (9999).: "))
    ano_atual =      int(input("Digite o ano atual (9999)...........: "))

    idade = ano_atual - ano_nascimento

    mensagem = f""""
    
        Nome completo (maiúsculo): {primeiro_nome.upper()} {sobrenome.upper()}
        Nome completo (minúsculo): {primeiro_nome.lower()} {sobrenome.lower()}
        
        Seja Bem vindo! {primeiro_nome} {sobrenome} ao sistema de cadastro. Você tem: {idade} anos e está autorizado de entrar no sistemas! 
        
    """
    print(mensagem)

processador_cadastro()