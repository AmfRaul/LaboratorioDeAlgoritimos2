 #Implemente um programa que compare o conteúdo de dois arquivos, lista1.txt e lista2.txt,
 #  onde cada um contém uma lista de produtos, com um produto por linha. O programa deve gerar um novo arquivo chamado diferenca.txt,
 #  que deve conter apenas os produtos que estão presentes em lista1.txt, mas ausentes em lista2.txt.
 #  Essa lista resultante deve ser salva no novo arquivo, com um produto por linha.

#Observação: Os arquivos lista1.txt e lista2.txt já existem e contêm dados.

def diferença():
    try:
        arquivo01 = open("aula-07/exerc-05/lista1.txt", "r+")
        arquivo02 = open("aula-07/exerc-05/lista2.txt")
        lista01 = arquivo01.read()
        lista02 = arquivo02.read()
        
        arquivo03 = open("aula-07/exerc-05/lista2.txt", "w")
        lista03 = arquivo03.read()

    
        if lista01 == lista02:
            lista01.write(lista03)
            print(lista03)


    except ImportError():
        print("[ERROR] de importação") 

def main():
    diferença()

main()