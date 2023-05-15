menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Que valor deseja depositar?"))

        if valor >= 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Valor inválido para deposito")

    elif opcao == "s":
        valor = float(input("Que valor deseja sacar?"))

        if valor <= saldo and numero_saques < LIMITE_SAQUES and valor <= limite:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print("Não foi possível realizar a operação!!")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inexistente, por favor selecione novamente a operação desejada.")