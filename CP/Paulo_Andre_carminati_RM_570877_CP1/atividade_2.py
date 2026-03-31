# "Desenvolva um programa em Python para cadastrar funcionários em um sistema corporativo.
# O programa deve solicitar três informações ao usuário e aplicar regras de formatação antes de exibi-las:

# Nome de Usuário: Solicite o nome completo.

# Departamento: Solicite a sigla ou nome do departamento. O programa deve garantir que o texto fique totalmente em letras maiúsculas (Ex: 'ti' deve virar 'TI').

# ID de Funcionário: Solicite o número de identificação e converta a entrada explicitamente para um número inteiro.

# Ao final, o programa deve utilizar f-strings para imprimir um relatório de confirmação exibindo os dados formatados."

def sistema_cadastro_corp():

    mensagem = """
    
        .......... CADASTRO DE FUNCIONÁRIOS - SISTEM-CORP .......... 
        
        
        Digite as informações abaixo solicitadas para o cadstro no sistem:
        
        
    """

    print(mensagem)

    nome =                     input("Primeiro nome...............: ")
    sobrenome =                input("Sobrenome...................: ")
    departamento =             input("Nome do departamento........: ")
    id_usuario =           int(input("Número de identificação.....: "))

    mensagem2 = f"""
    
        ++++++++++ DADOS DO FUNCIONÁRIO ++++++++++
        
        
        Nome................................: {nome} {sobrenome}
        Departamento........................: {departamento.upper()}
        ID Usuário (número de identificação.: {id_usuario} 
        
        
        
        ++++++++++ CADASTRO REALIZADO COM SUCESSO ++++++++++
        
        
    """
    print(mensagem2)

sistema_cadastro_corp()

