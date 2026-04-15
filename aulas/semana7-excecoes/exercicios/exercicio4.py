# Atividade pratica 2: validacao de saque

## crie um progrma que simula um saque em uma conta

## defina uma variavel saldo_conta com valor (ex: 5000)

## Dentro de um bloco try, peça ao usuário o valor do saque e verifique se ele é maior que o saldo

## Se o valor do saque for maior, lance um VallueError com a mensagem "saldo insuficinete"

## Se o saque for válido, calcule e exiba o novo saldo no bloco else.abs

## Use o bloco except para capturar o VallueError e exibir a mensagem de erro.abs

# ---------------------------------------------------------------------------------------------------------

while True:

    print(""" 
        Validação de saque

        1 - Sacar
        2 - Verificar o saldo
        
        0 - sair

    """)

    saldo_conta = 500.000

    opcao = int(input("Digite a operação desejada: "))

    
    
    try:

        if(opcao == 1):
            sacar = saldo_conta - valor
            
            valor(float(input("Digite o valor do saque: ")))

            if(valor > saldo_conta):
                raise ValueError("Saldo insuficiente!")
            else:
                print(f"""

                    Saque realizado com sucesso!
                    
                    - Valor sacado...: R$ {valor}
                    - Saldo Restanto.: R$ {saldo_conta}

                """)
        elif(opcao == 2):
            print("""
                Saldo da conta:

                - Saldo atual: R$ {saldo_conta}
            """)

        elif (opcao == 0):
            print("Saindo da aplicação!")
            break


    except ValueError:
        print("Erro! Operação não autorizada - Digite um número inteiro!")
    finally:
        print("Obrigado por usar o sistema!")


        

        

        