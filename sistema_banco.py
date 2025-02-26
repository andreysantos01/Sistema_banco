#sistema de Banco onde é permitido três saques com limite de R$ 500 por saque, onde imprimi as operações realizadas
from datetime import datetime

def depositar(saldo, valor, extrato):
    if valor > 0:
        print("Depósito realizado com sucesso!")
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! Valor inválido.")
    return saldo, extrato

def sacar(valor, saldo, extrato, saques_realizados, LIMITE_SAQUES, limite_valor_saque):
    if saques_realizados >= LIMITE_SAQUES:
        print("Operação falhou! Limite de saques diários atingido.")
    elif valor > limite_valor_saque:
        print("Operação falhou! Valor do saque excede o limite permitido.")
    elif valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    else:
        print("Saque realizado com sucesso!")
        saldo -= valor
        saques_realizados += 1
        extrato += f"Saque: R$ {valor:.2f}\n"
        return saldo, extrato, saques_realizados
    return saldo, extrato, saques_realizados

def imprimir_extrato(saldo, extrato):
    hora = datetime.now()
    hora_format = datetime.strftime(hora, "%d/%m/%Y %H:%M:%S")

    print("\n========== Extrato ==========")
    print(f"{hora_format}\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_usuario(cpf, usuarios):
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Digite seu nome: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla do estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(linha)

def menu():
    print('''\n========= Banco A.A =========
    [1] - Depósito
    [2] - Saque
    [3] - Extrato
    [4] - Novo usuário
    [5] - Nova conta
    [6] - Listar contas
    [7] - Sair
    ''')
    opcao = int(input("Escolha uma opção: "))
    return opcao

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    saldo = 0
    limite_valor_saque = 500
    saques_realizados = 0
    extrato = ""
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Digite o valor a depositar: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == 2:
            valor = float(input("Digite o valor do saque: R$ "))
            saldo, extrato, saques_realizados = sacar(valor, saldo, extrato, saques_realizados, LIMITE_SAQUES, limite_valor_saque)
        elif opcao == 3:
            imprimir_extrato(saldo, extrato)
        elif opcao == 4:
            criar_usuario(usuarios)
        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == 6:
            listar_contas(contas)
        elif opcao == 7:
            print("\n================================")
            print("\nObrigado por usar o Banco A.A!")
            print("\n================================")
            break
        else:
            print("Opção inválida, escolha novamente a opção desejada")

if __name__ == "__main__":
    main()