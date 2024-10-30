#Crie uma função que recebe um ano através de um input e defina se o mesmo é bissexto ou não. Utilize as seguintes
#regras: Um ano bissexto é divisível por 4, mas não por 100, ou então se é divisível por 400. Exemplo: 1988 é bissexto pois
#é divisível por 4 e não é por 100; 2000 é bissexto porque é divisível por 400.

def bissexto(ano):
        divisao = ano % 4
        if divisao == 0:
            print(f"O ano {ano} é bissexto")
        else:
            print(f"O ano {ano} NÂO é bissexto")

def main():
    print("DIGITE -- 0 -- para concluir")
    while True:
        opc = 0
        try:
            ano = int(input("Digite um ano: "))
            if ano == opc:
                break
            logica = bissexto(ano)
            continue

        except ValueError:
            print("< [ERROR] numero invalido >")
    
main()