#4. Utilizando dicionários, crie um programa que simule um caixa eletrônico. O usuário poderá optar pelas
#seguintes funcionalidades:

#Depositar dinheiro – Usuário pode depositar valor ilimitado, desde que seja positivo;
#Sacar dinheiro – Usuário pode sacar um valor limitado que deve ser validado pelo campo
#“transaction_limit”;
#Verificar saldo bancário – Usuário pode consultar o saldo atual;
#Sair – Usuário pode sair do sistema.

#Lembre de tratar exceções. Para criar o programa, utilize a seguinte estrutura de dicionário:

def deposito(conta_banco):
    try:
        valor_deposito = float(input("Digite um valor de deposito: "))
        conta_banco["saldo"] += valor_deposito
    except ValueError:
        print("[ERROR] valor digitado invalido")
    

def sacar(conta_banco):
    try:
        valor_saque = float(input("Coloque um valor para saque: "))
        if valor_saque < conta_banco["saldo"]:
            subtração = conta_banco["saldo"] - valor_saque
            conta_banco["saldo"] = subtração
            print("Valor sacado R$ ",valor_saque)
        else:
            print("<Valor indisponivel na conta>")
    except ValueError:
        print("[ERROR] valor digitado invalido")
def verificar_saldo(conta_banco):
    print("saldo disponivel R$",conta_banco["saldo"])

def main():
    print("1- Deposito"
          "2- Saque"
          "3- Verificar Saldo"
          "4- Sair")
        
    conta_banco = {
        "saldo" : 0,
        "saque" : 0
    }
    

    while True:
        opc = 0 
        opcoes = int(input("Digite uma opção: "))
        if opcoes == 1:
            deposito(conta_banco)
        if opcoes == 2:
            sacar(conta_banco)
        if opcoes == 3:
            verificar_saldo(conta_banco)
        if opcoes == 4:
            break

main()