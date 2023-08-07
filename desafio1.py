menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito no valor de {valor:.2f} realizado.")
        else:
            print("Operação inválida. Por favor, insira um valor válido.")

    elif opcao == "s":
        print("Saque")
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_limite_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação inválida. Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação inválida. O valor máximo de saque é de R$500,00.")
        elif excedeu_limite_saques:
            print(
                "Operação inválida. O número máximo de saques diários já foi alcançado.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Saque no valor de {valor:.2f} realizado.")
            numero_saques += 1
        else:
            print("Operação inválida. Por favor, insira um valor válido.")

    elif opcao == "e":
        print(" Extrato ".center(16, "="))
        print("Não foram realizadas movimentações na conta" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
