# Crie um método que receba uma lista com elementos duplicados.
#  Ela deve gerar uma lista com os elementos que estava duplicados e uma lista com os elementos unificados.

def lista_duplicados(lista1):
    lista2 = []
    lista3 = []

    for numer in range(len(lista1)):
        if lista1[numer] not in lista3:
            lista3.append(lista1[numer])
        else:
            lista2.append(lista1[numer])

    return lista2, lista3

def main():
    lista1 = [2,3,3,5,4,2,6,7,8,2]

    lista2, lista3 = lista_duplicados(lista1)
    
    print("Itens duplicados: ", lista3)
    print("Itens não duplicados: ", lista2)



main()