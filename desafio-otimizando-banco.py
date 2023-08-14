# mini banco
import textwrap

def menu():
    menu = """\n
    ============= menu ==============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def criar_usuarios(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuário(cpf, usuarios)

    if usuario:
        print("Já existe um usuário cadastrado com esse CPF!")
        return
    
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento (dd-mm-aaaa): ")
    endereço = input("Informe o seu endereço (rua - nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})
    print("## Usuário criado com sucesso! ##")

def filtrar_usuário(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuário(cpf, usuarios)

    if usuario:
        print("\n Conta Criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuário não encontrado, fluxo de criação de conta encerrado! ")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if limite_saques > 0:
        if saldo > 0 and valor < saldo:
            if valor > limite:
                saldo -= valor
                limite_saques -= 1
                numero_saques += 1
                extrato += f"Valor do saque efetuado => R$ {valor:.2f}, Saldo => R$ {saldo:.2f} \n"
                print("Processando Saque... \n Retire as Cédulas abaixo. \n Saque efetuado com sucesso!")
            else:
                print("O valor do saque excede o limite.")
        else:
            print("Saldo insuficiente.")
    else:
        print("Limite de saques diários excedido.")

    return saldo, extrato

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Valor depositado => R$ {valor:.2f}, Saldo => R$ {saldo:.2f} \n"
        print(f"Deposito de R$ {valor:.2f} efetuado com sucesso!")
    else:
        print("\nO valor informado é inválido.")
    return saldo, extrato

def extrato(saldo, /, *, extrato):
    print("Extrato".center(13, "#"), end="\n")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print(extrato, end="\n")
    return extrato

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numeros_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "s":
            valor = float(input("Valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numeros_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "d":
            valor = float(input("Valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "e":
            extrato(saldo, extrato=extrato)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "nu":
            criar_usuarios(usuarios)

        elif opcao == "q": # sair
            print("Saindo...")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
