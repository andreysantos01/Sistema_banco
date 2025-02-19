#sistema de Banco onde é permitido três saques com limite de R$ 500 por saque, onde imprimi as operações realizadas

saldo = 0
limite_saques = 3
limite_valor_saque = 500
saques_realizados = 0 
depositos_realizados = 0
extrato = ""

while True:
    print(''' **** Banco A.A ****
          [1] - Depósito
          [2] - Saque
          [3] - Extrato
          [4]- Sair
          ''')
    menu = int(input(": "))
    if menu == 1:
        deposito = float(input("Digite o valor a depositar R$ "))
        if deposito <0:
            print("Valor inválido !")
        else:
            print("Deposito com sucesso !")
            saldo +=deposito
            depositos_realizados +=1
            extrato += f"Depósito {deposito:.2f}  sss"
    elif menu == 2:
        valor_sacado = float(input("Digite o valor do saque R$ "))
        if saques_realizados > limite_saques:
            print("Limite de saques diário atingido !")
        elif valor_sacado > limite_valor_saque:
            print("Saque inválido, saque permitido é de R$ 500")
        elif valor_sacado > saldo:
            print("limite insuficiente ")
        else:
            print("Saque realizado com sucesso !")
            saldo -= valor_sacado
            saques_realizados +=1
            extrato += f"\nSaque: R$ {valor_sacado:.2F}\n"
    elif menu == 3:
        print("\n ========== Extrato ==========")
        print("Não foram realizadas movimentações. " if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
    elif menu == 4:
        print("Obrigado por usar o Banco A.A")
        break
    else:
        print("Opção invalida, escolha novamnete a opção desejada")
    

