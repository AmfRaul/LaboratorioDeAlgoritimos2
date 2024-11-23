import random

def tabela():
    #cria uma tabela de 7x7 e da um append dos quadros brancos
    tabela = []
    for linha in range(7):
        linha = []
        for coluna in range(7):
            linha.append("⬜")
        tabela.append(linha)

    return tabela

def gerar_minas(tabela):
    #gera as minas com um loop while ate que atinja as 20 minas e adiciona a tabela
    minas = 0
    while minas < 20:
        PosicaoX = random.randint(0, 6)
        PosicaoY = random.randint(0, 6)
        if tabela[PosicaoX][PosicaoY] != "💣": 
            tabela[PosicaoX][PosicaoY] = "💣" 
            minas += 1

def mostrar_tabela(tabela):
    print("  0  1  2  3  4  5  6")
    i = 0
    for linha in tabela:
        print(f"{i} {' '.join(linha)}") # faz que vire uma string e tira as aspas da matriz 
        i += 1

def contar_minas_ao_redor(tabela, x, y):
    minas = 0

    direcoes = [(-1, -1), (-1, 0), (-1, 1),  # Posições ao redor
                (0, -1),         (0, 1),
                (1, -1), (1, 0), (1, 1)]

    for dx, dy in direcoes:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 7 and 0 <= ny < 7:  # Verifica se está dentro do tabuleiro
            if tabela[nx][ny] == "💣":  # Verifica se a posição contém uma mina
                minas += 1

    return minas
#def score():
   # try:
  #      arquivo = open("informacaoPessoal.txt", "r")

 #   except
 #
def pontuacoes():
    arquivo = open("score.txt", "r")
    lista = arquivo.readlines()
    
    try:
        nome = input("Digite seu nome para ver sua pontuação: ")
        encontrou = False
        for linha in lista:
            nome_na_linha = ''
            for caractere in linha:
                if caractere == ':':
                    break
                nome_na_linha += caractere
            
            nome_na_linha = nome_na_linha.strip()
            if nome == nome_na_linha:
                print(linha.strip())
                encontrou = True
        else:
            print(f"A pessoa com nome {nome} não ha pontuações salvas")
    
    except ValueError:
        print("[ERROR] nome digitado invalido")
    
    arquivo.close()



def iniciar_jogo():
    while True:
        nome = input("Digite seu nome: > ")
        if nome == "": 
            print("[ERROR] Valor digitado inválido") 
            continue 
        break
    tabela_criada = tabela()
    gerar_minas(tabela_criada)
    tabela_visivel = tabela()


    while True:
        score = 0
        mostrar_tabela(tabela_visivel)
        
        try:
            posicaoX = int(input("Digite a posicao X (0, 6): "))
            posicaoY = int(input("DIgite a posicao Y (0, 6): "))

        except ValueError:
            print("[ERROR] valor digitado invalido :( ")
            continue



        #VER SE NAO FOI DIGITADO UM VALOR SUPERIOR OU INFERIOR AO PEDIDO
        if posicaoX > 6 or posicaoX < 0:
            print("\n Digite um numero entre os intervalos pedidos \n ")
            continue
        elif posicaoY > 6 or posicaoY < 0:
            print("\n Digite um numero entre os intervalos pedidos \n")
            continue
            


        #MOSTRAR MENSAGEM QUE PERDEU
        if tabela_criada[posicaoX][posicaoY] == "💣":
            mostrar_tabela(tabela_criada)
            print("Infelizmente voce perdeu! MINA ENCONTRADA 💣 ")
            arquivo = open("score.txt", "a")
            arquivo.writelines(f"{nome} : {score}\n")
            arquivo.close()
            break



        #CONTINUAR O JOGO SE NAO FOR ENCONTRADO NENHUMA MINA
        else: 
            minas_ao_redor = contar_minas_ao_redor(tabela_criada, posicaoX, posicaoY)
            tabela_visivel[posicaoX][posicaoY] = str(minas_ao_redor) 
            score += 1

        


        #VER SE GANHOU O JOGO
        casas_abertas = True
        for linha in range(7):
            for coluna in range(7):
                if tabela_criada[linha][coluna] != "⬜":
                    casas_abertas = False
                    break
            if not casas_abertas:
                break
        if casas_abertas:
            arquivo = open("score.txt", "a")
            print("<< MEUS PARABENS >>")
            print("  < VOCE GANHOU >  ")
            print(f"{nome}= {score} pontos")
            arquivo.writelines(f"{nome} = {score}\n")
            arquivo.close()
            break


