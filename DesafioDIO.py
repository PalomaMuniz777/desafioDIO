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
    opcao = input(menu).lower()  # Converte a opção para minúsculas para facilitar a comparação

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Valor do depósito inválido. Tente novamente.")
        except ValueError:
            print("Formato de valor inválido. Utilize números decimais.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Saldo insuficiente para saque.")
            elif excedeu_limite:
                print("Valor do saque excede o limite.")
            elif excedeu_saques:
                print("Número máximo de saques por dia excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Valor do saque inválido. Tente novamente.")
        except ValueError:
            print("Formato de valor inválido. Utilize números decimais.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
