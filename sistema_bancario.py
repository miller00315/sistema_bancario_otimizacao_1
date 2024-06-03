import textwrap

def menu():
    menu = """\n
========= MENU ============
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nc]\tNova conta
[lc]\tListar contas
[nu]\tNovo usuário
[q]\tSair
=>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\t R$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso")
    else:
        print("\n Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n Operação falhou! Você não tem saldo o suficiente.")

    elif excedeu_limite:
        print("\n Operação falhou! O valor do saque excede o limite.")
    
    elif excedeu_saques:
        print("\n Operação falhou! Número máximo de saques excedidos.")

    elif valor > 0:
        saldo -= valor
        extrato += f"\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso\n")
    
    else:
        print("\n Operação falhou! o valor informado é inválido\n")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================= EXTRATO ================")
    print("\nNão foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("\n==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF: (somente números)")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n já existe um usuário com este nome.\n")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro -bairro - cidade/sigla estado)")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n Usuário criado com sucesso!\n")
    

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário")

    usuario = filtrar_usuario(cpf, usuarios)

    if(usuario):
        print("\n numero de conta criado com sucesso! \n")

        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuário não encontrado, fluxo de criaçã de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """

        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        match opcao:
            case "d":
                valor = float(input("Informe o valor do depósito: "))

                saldo, extrato = depositar(saldo, valor, extrato)

            case "s":
                valor = float(input("Informe o valor do saque: "))

                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES
                )
            case "e":
                exibir_extrato(saldo, extrato=extrato)

            case "nu":
                criar_usuario(usuarios)
            
            case "nc":
                numero_conta = len(contas) + 1

                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                contas.append(conta)
            case "q":
                break

            case _:
                print("Opção inválida")

    return


main()