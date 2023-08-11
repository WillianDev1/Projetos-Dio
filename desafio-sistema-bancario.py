# mini banco

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d": # deposito
        valor = float(input("Qual o valor do deposito: "))
        saldo += valor
        extrato += f"Valor depositado => R$ {valor:.2f}, Saldo => R$ {saldo:.2f} \n"
        print(f"Deposito de R$ {valor:.2f} efetuado com sucesso!")

    elif opcao == "s": # saque
        valor = float(input("Quanto deseja sacar: "))

        if LIMITE_SAQUES > 0:
            if saldo > 0 and valor < saldo:
                saldo -= valor
                LIMITE_SAQUES -= 1
                numeros_saques += 1
                extrato += f"Valor do saque efetuado => R$ {valor:.2f}, Saldo => R$ {saldo:.2f} \n"
                print("Processando Saque... \n Retire as Cédulas abaixo. \n Saque efetuado com sucesso!")
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite de saques diários excedido.")

    elif opcao == "e": # extrato
        print("Extrato".center(13, "#"), end="\n")
        print(extrato, end="\n")
        print("Quantidade de Saques Efetuados => ", numeros_saques)

    elif opcao == "q": # sair
        print("Saindo...")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
