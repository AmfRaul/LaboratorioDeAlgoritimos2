#Sacar: Permite ao usuário retirar um valor, desde que haja saldo suficiente.

def sacar():
    try:
        while True:
            banco = open("modules/banco.txt", "r+")
            lista = banco.readlines()
            print(lista)


            quantidade = float(input("Digite a quantidade desejada para saque:"))

            banco.write(quantidade)
            print(banco.read())

            banco.close()
    except:
        print("ERROR")

    