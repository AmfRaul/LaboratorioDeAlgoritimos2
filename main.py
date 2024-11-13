from modules.menuBanco import menu
from modules.saque import sacar
from modules.deposito import depositar_dinheiro
from modules.consultar_saldo import consultar_Saldo
from modules.extrato import extrato

def main():
    while True:
        opcao = menu()

        if opcao == 1:
            quantidade = float(input("Digite a quantidade desejada para saque:"))   
            sacar(quantidade)
        elif opcao == 2:
            depos = float(input("Digite o valor de deposito: "))
            depositar_dinheiro(depos)
        elif opcao == 3:
            consultar_Saldo()
        elif opcao == 4:
            extrato()
        elif opcao == 5:
            print("VOCE SAIU< = ATE MAIS!!")
main()