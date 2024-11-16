# Desenvolva um programa que leia o conteúdo de um arquivo chamado texto.txt e conte o número total de palavras contidas nele.
# O programa deve exibir essa contagem para o usuário. Caso o arquivo texto.txt não exista,
# exiba uma mensagem de erro informando a ausência do arquivo e encerre o programa. Dica: 
# use o método split() para separar as palavras em cada linha, considerando que elas são delimitadas por espaços.

#Observação: O arquivo texto.txt já existe e contém dados

def ler_conteudo():
    try:
        arquivo = open("aula-07/exerc-04/texto.txt")
        lista_modificavel = arquivo.read()
        palavras = lista_modificavel.split()
        
        quantidade_palavras = 0
        em_palavra = False

        
        for x in palavras:
            if x not in [' ', '\n', '\t', '.', ',', '!', '?', ';', ':', '-', '(', ')', '"', "'"]:
                if not em_palavra:
                    quantidade_palavras += 1 
                    em_palavra = True 
                else:
                    em_palavra = False
        print(quantidade_palavras * 2)
        arquivo.close()
    except FileNotFoundError:
        print("[ERROR] arquivo nao econtrado")
    

def main():
    ler_conteudo()

main()