
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
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo = saldo + valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inserido é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if LIMITE_SAQUES == 0:
            print(f"Você execedeu o limite de 3 saques diários.")
    
        elif valor > saldo:
            print(f"Saldo insuficiente para fazer o saque.")
        
        elif valor > limite:
            print(f"Valor de saque superior ao limite diário de R$ {limite}.00")

        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            LIMITE_SAQUES -= 1
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
