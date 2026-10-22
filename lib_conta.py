#Blibioteca de funções da conta corrente
conta_saldo = 0
conta_extrato = None

def depositar(valor):

    if valor > 0:

        global conta_saldo
        global conta_extrato

        conta_saldo += valor
        if conta_extrato is None:
            conta_extrato = f"Deposito efetuado no valor de R$ {valor}\n"
        else:
            conta_extrato += f"Deposito efetuado no valor de R$ {valor}\n"

        return True
    
    return False

def sacar(valor):
    
    global conta_saldo
    global conta_extrato

    if valor > 0 and conta_saldo > valor:

        conta_saldo -= valor
        conta_extrato += f"Saque efetuado no valor de R$ {valor}\n"

        return True
    
    return False

def extrato():
    if conta_extrato is None:
        return f"Extrato vazio"
    
    return conta_extrato

def saldo():
    return conta_saldo