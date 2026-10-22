from lib_conta import *

def exibir_menu():
    print(">>> Gestão de Conta Corrente <<<")
    print("================================")
    print("== 1 - Depositar              ==")
    print("== 2 - Sacar                  ==")
    print("== 3 - Exibir Saldo           ==")
    print("== 4 - Exibir Extrato         ==")
    print("== 0 - Sair                   ==")
    print("================================")

    #Loop principal
while True:

    exibir_menu()
    select = input("Digite a opção desejada: ")

    #Sair
    if select == '0':
        break

    #Deposito
    elif select == '1':
        try:
            #Aceitar apenas números
            valor = float(input("Digite o valor que deseja depositar: "))
            #Validação do valor
            if not depositar(valor):
                print("Valor Invalido")
                input("Pressione enter para continuar...")
                continue

        except ValueError:
            print("Digite apenas números")
            input("Pressione enter para continuar...")
            continue

    elif select == '3':
        print("\n===================")
        print(f"Saldo: R$ {saldo():.2f}")
        print("====================")
        input("Pressione enter para continuar...")
        continue

    elif select == '4':
        print("\n===================\n")
        print(extrato())
        print("====================")
        input("Pressione enter para continuar...")
        continue

    else:
        print("Opção Invalida")
        input("Pressione enter para continuar...")
        continue
