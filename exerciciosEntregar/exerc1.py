
def intervalo(entrada):
    inicio = 0
    fim = 0
    ListaIntervalo = []

    for num in entrada:
        if entrada == fim + 1:
            fim = entrada
        else:
            ListaIntervalo.append((inicio, fim))
            inicio = fim = entrada
    ListaIntervalo.append((inicio,fim))
    print(ListaIntervalo)

    return ListaIntervalo

entrada = [100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150]
