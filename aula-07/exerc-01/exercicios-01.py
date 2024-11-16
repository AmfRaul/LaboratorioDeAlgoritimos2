#1. Desenvolva um programa que leia e exiba o conteúdo de um arquivo chamado nomes.txt, onde cada linha contém o nome de uma pessoa.
#O programa deve exibir cada nome em uma linha separada na tela. Caso o arquivo nomes.txt não exista, 
#o programa deve exibir uma mensagem de erro informativa e encerrar de forma segura.

def exibir_nomes():
    try:
        arquivo = open("aula-07/nomes.txt", "r")

        lista = arquivo.readlines()
        for i in lista:
            print(i.strip())



        arquivo.close()
    except OSError:
        print("ERROR")

def main():
    exibir_nomes()

main()