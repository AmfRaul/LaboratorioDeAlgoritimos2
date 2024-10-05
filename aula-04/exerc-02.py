#Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em
#um dicionário, onde a chave é a vogal considerada.
vogais = ["a", "e", "i", "o", "u"]
dicionario = {}


vogais_informada = input("Digite uma palavra:  ")
dicionario["chave"] = vogais_informada 

for letras in range(len(dicionario)):
    print(letras)
    if letras in vogais:
        dicionario[letras] += 1
    print(letras) 