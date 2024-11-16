#3. Crie um programa que leia o conteúdo de um arquivo chamado artigo.txt e conte quantas vezes cada palavra aparece no texto.  
#O programa deve exibir um relatório na tela, listando cada palavra acompanhada de sua respectiva contagem.
#  Desconsidere diferenças de maiúsculas e minúsculas para a contagem e remova pontuações para evitar duplicidade de palavras.

#Observação: O arquivo artigo.txt já existe e contém dados.

def contar_palavras(palavra):
    try:
        lista_palavras = open("aula-07/exerc-03/artigo.txt", "r")
        lista_modificavel = lista_palavras.read()
        
        while True:
            
            if palavra == "sair":
                print("<< VOCE SAIU >>")
                break

            if palavra in lista_modificavel:
                print(f"A palavra {palavra} esta na lista")

            else:
                print("<< Palavra não encontrada >>")
                palavra
        lista_palavras.close()
    except ValueError:
        print("[ERROR] valor digitado invalido")
    
def main():
    
    palavra = input("Digite a palavra que deseja encontrar: ")
    contar_palavras(palavra)

main()