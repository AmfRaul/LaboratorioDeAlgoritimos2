#Escreva um programa que solicite ao usuário um número inteiro x, representando 
#a quantidade de números aleatórios a serem gerados. O programa deve então criar um arquivo chamado numeros.txt
#e gravar x números aleatórios no intervalo de 0 a 100, cada um em uma linha. 
#Certifique-se de que o arquivo seja gerado com os números na quantidade e no intervalo especificados.

import random 

def numero_inteiro():
    while True:

        quantidade = int(input("Digite a quantidade de numeros aleatorios para ser gerados: "))
        numeros = []

        for i in range(quantidade):
            numeros_aleatorios = random.randint(0,100)
            numeros.append(numeros_aleatorios)

        arquivo = open("aula-07/exerc-02/numeros.txt", "w")
        for numero in numeros:
            arquivo.write(f"{numero}\n")
        arquivo.close()

        for numero in numeros:
            print(numero)

numero_inteiro()