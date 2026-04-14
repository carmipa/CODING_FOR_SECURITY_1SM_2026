nome =               input("Digite seu primeiro nome...................: ")
sobrenome =          input("Digite seu sobrenome.......................: ")
try:
    ano_nascimento = int(input("Digite seu ano de nascimento(ex: 1990).: "))
    
    idade = 2026 - ano_nascimento
    
    print(f"""
        Ola, Meu nome é {nome} {sobrenome} e eu tenho {idade} anos.
    """)
    
except ValueError:
    print("\n[x] Erro! Digite apenas números para o ano de nascimento (ex: 2005). Letras/texto não são aceitos! [x]")