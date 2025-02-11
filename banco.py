menu = """\n
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo = 0
limite = 500
numero_saques = 0
transacoes = ""
LIMITE_SAQUES = 3


def depositar():

    global saldo, transacoes
    print("-=" * 10)
    print(" DEPÓSITO ".center(20, "="))
    print("-=" * 10)
   
    valor = float(input("\nInsira o valor desejado para o depósito: R$ "))

    if valor > 0:
        saldo += valor
        transacoes += f"\n{'-=' * 5}\nDEPÓSITO: R$ {valor:.2f}\n{'-=' * 5}"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação inválida! Insira valores positivos para o depósito.")

    print("-=" * 10)


def sacar():
    global saldo, numero_saques, transacoes

    print("-=" * 10)
    print(" SAQUE ".center(20, "="))
    print("-=" * 10)
    
    saque = float(input("\nQuanto você quer sacar? R$ "))


    if saque <= 0:
        print("Valor inválido! O saque deve ser maior que zero.")
    elif numero_saques < LIMITE_SAQUES and saque <= limite:
        if saque > saldo:
            print("Não é possível sacar um valor maior do que o saldo da sua conta!")
        else:
            transacoes += f"\n{'=' * 20}\nSAQUE: R$ {saque:.2f}\n{'=' * 20}"
            numero_saques += 1
            saldo -= saque
            print("Sacando...")
    elif numero_saques >= LIMITE_SAQUES:
        print("Número de saques diários atingido! Tente novamente amanhã.")
    else:
        print(f"Você só pode sacar até R$ {limite:.2f} por vez.")

    print("-=" * 10)


def extrato():
    print("\n" + "-=" * 15)
    print(" EXTRATO ".center(30, "="))
    print("-=" * 15)

    print(transacoes if transacoes else "Nenhuma movimentação realizada.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")

    print("-=" * 15)


while True:
    opcao = input(menu).strip().lower()

    if opcao == 'd':
        depositar()

    elif opcao == 's':
        sacar()

    elif opcao == 'e':
        extrato()

    elif opcao == 'q':
        print("\nSaindo... Obrigado por usar nosso sistema!")
        print("-=" * 15)
        break

    else:
        print("Operação inválida! Por favor, selecione novamente a opção desejada.")
