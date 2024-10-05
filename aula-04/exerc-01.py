#Escreva um programa em Python que verifique se uma chave existe ou não em um dicionário. Se a
#chave existir no dicionário, imprima Verdadeiro. Caso contrário, imprima Falso.

dicionario = {}

chave = input("Digite uma chave: ")
dicionario["chave"] = chave

chave_informada = input("Digite uma chave para ver se esta na lista: ")

if chave_informada in dicionario:
    print("A chave esta no dicionario")
else:
    print("A chave NAO esta no dicionario")

