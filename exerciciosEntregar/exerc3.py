#Escreva um programa que realize a transposição de uma matriz (linhas se tornam colunas e vice-versa).

def matrizes(matriz):
    for linhas in range(len(matriz)):
        for colunas in range(len(matriz[0])):
            novaMatriz = []
    for x in range(linhas):
        linha = []
        for y in range(colunas):
            linha.append(matriz[y][x])
        novaMatriz.append(linha)

    return novaMatriz    

matriz = [
    [5, 2, 1],
    [1, 5, 6],
    [7, 4, 5]
]

novaMatriz = matrizes(matriz)
for linha in novaMatriz:
    print(novaMatriz)