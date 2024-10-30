#Crie um programa que receba através de input dois números e retorne sua divisão.
def divisao(num_01, num_02):
    try:
        resultado = num_01 / num_02
        print("O resultado da divisão é: ", resultado)
    except ZeroDivisionError:
        print(f"[ERROR] houve um erro de divisao")



def main():
    while True:
        try:
            num_01 = int(input("Digite o primeiro numero: "))
            num_02 = int(input("Digite o segundo numero: "))

            dividir = divisao(num_01, num_02)

            return dividir
        except ValueError:
            print("[ERROR] ocorreu um erro de valor ")

main()