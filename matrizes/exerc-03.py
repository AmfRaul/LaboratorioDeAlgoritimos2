def escontrar_valor(matriz):
    menorValor = 999999999


    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            matriz[linha][coluna]
            # matriz[linha][coluna] = isso armazena o valor em questao
            if matriz[linha][coluna] <= menorValor:
                menorValor = matriz[linha][coluna] 
                print(menorValor)
    return menorValor


matriz = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
]
escontrar_valor(matriz)
        