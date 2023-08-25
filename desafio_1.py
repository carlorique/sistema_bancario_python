saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("\nEscolha uma operação: ")
    print("[1] DEPOSITAR")
    print("[2] SACAR")
    print("[3] EXTRATO")
    print("[4] SAIR")

    escolha = int(input("Digite o numero da operação: "))
    
    if escolha == 1:
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: {valor:.2f}\n"
        else:
            print("Operação falhou! o valor informado é inválido.")
    elif escolha == 2:
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou com! Você nao tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! o valor do saque excedeu o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! Informe o valor informado é inválido.")
    elif escolha == 3:
        print("\n################## EXTRATO ##################")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("\n#############################################")
    elif escolha == 4:
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
