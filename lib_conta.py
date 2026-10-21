#Blibiote de funções da conta corrente
conta_saldo = 0
conta_extrato = ""

def deposito(valor):

    if valor > 0:

        global conta_saldo
        global conta_extrato

        conta_saldo += valor
        conta_extrato += f"Deposito efetuado no valor de R$ {valor}"

        return True
    
    return False

def saque(valor):
    
    global conta_saldo
    global conta_extrato

    if valor > 0 and conta_saldo > valor:

        conta_saldo -= valor
        conta_extrato += f"Saque efetuado no valor de R$ {valor}"

        return True
    
    return False

def extrato():
    return conta_extrato

def saldo():
    return conta_saldo