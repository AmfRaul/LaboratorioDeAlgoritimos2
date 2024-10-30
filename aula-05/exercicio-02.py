#2. Crie um programa que receba através de um input o valor numérico de um mês e retorne seu valor escrito. Lembre
#de tratar as exceções do seu programa. Exemplo: 1 -> Janeiro, 12 -> Dezembro

def mes(meses):
    while True:
        try:
            digite = int(input("Digite o numero do mes escolhido: "))
            for chave in meses:
                if digite == chave:
                    print(f"> {chave}- {meses[chave]}")
        except ValueError:
            print("[ERROR] Valor informado incorreto")
        break
def main():
    meses = {
        "1": "janeiro",
        "2" : "fevereiro",
        "3" : "março",
        "4" : "abril",
        "5" : "maio",
        "6" : "junho" ,
        "7" : "julho",
        "8" : "agosto",
        "9" : "setembro",
        "10" : "outubro",
        "11" : "novembro",
        "12" : "dezembro"
    }
    mes(meses)


main()
