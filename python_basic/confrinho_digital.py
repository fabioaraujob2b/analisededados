saldo = 0.0
while True:
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Saldo")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        try:
            valor = float(input("Digite o valor a ser depositado: "))
            if valor <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
            else:
                saldo += valor
                print("Depósito realizado com sucesso!")
        except ValueError:
            print("Valor inválido, tente novamente.")
    elif opcao == 2:
        try:
            saque = float(input("Digite o valor a ser sacado: "))
            if saque <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
            elif saque > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= saque
                print("Saque realizado com sucesso!")
        except ValueError:
            print("Valor inválido, tente novamente.")
    elif opcao == 3:
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == 4:
        print("Saindo...")
        break
    else: 
        print("Opção inválida, tente novamente.")