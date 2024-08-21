menu = "[1] - Depositar, [2] - Saque, [3] - Extrato, [0] - Sair"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu + "\nEscolha uma opção: ")
    
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Houve um erro na operação! Digite um valor válido.")
    
    elif opcao == "2":
        valor = float(input("Digite o valor a ser sacado: "))
        
        passou_saldo = valor > saldo
        passou_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if passou_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif passou_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "3":
        print("\nExtrato:")
        if extrato:
            print(extrato)
        else:
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo atual: R$ {saldo:.2f}\n")
    
    elif opcao == "0":
        print("Saindo do sistema... Obrigado por utilizar nossos serviços!")
        break
    
    else:
        print("Operação inválida! Por favor, selecione uma opção válida.")
