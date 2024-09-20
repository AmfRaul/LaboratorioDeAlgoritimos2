import random

def nova_cartela():
    cartela = []
    for linha in range(5):
        linha_numeros = []
        for coluna in range(5):
            while True:
                numero = random.randint(0, 99)
                if numero not in linha_numeros:
                    linha_numeros.append(numero)
                    break
        cartela.append(linha_numeros)
    return cartela

def mostrar_cartela(cartela):
    for linha in cartela:
        for numero in linha:
            print(numero, end="\t")
        print("")

def main():
    cartela = nova_cartela()
    print("Cartela de Bingo:")
    mostrar_cartela(cartela)

main()