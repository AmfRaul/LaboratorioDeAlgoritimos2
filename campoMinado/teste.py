
import random

# Função para criar o tabuleiro 7x7 com quadrados brancos (⬜)
def tabela():
    tabela = []
    for linha in range(7):
        linha = []
        for coluna in range(7):
            linha.append("⬜")
        tabela.append(linha)
    return tabela

# Função para gerar 20 minas no tabuleiro
def gerar_minas(tabela):
    minas = 0
    while minas < 20:
        posicaoX = random.randint(0, 6)
        posicaoY = random.randint(0, 6)
        if tabela[posicaoX][posicaoY] != "💣":
            tabela[posicaoX][posicaoY] = "💣"
            minas += 1

# Função para mostrar o tabuleiro no console
def mostrar_tabela(tabelas):
    print("  0  1  2  3  4  5  6")
    for i, linhas in enumerate(tabelas):
        print(f"{i} {' '.join(linhas)}")

# Função para contar o número de minas ao redor de uma célula específica no tabuleiro
def contar_minas_ao_redor(tabela, x, y):
    """Conta o número de minas ao redor de uma célula específica no tabuleiro."""
    direcoes = [(-1, -1), (-1, 0), (-1, 1),  # Direções ao redor da célula
                (0, -1),         (0, 1),
                (1, -1), (1, 0), (1, 1)]
    minas = 0

    for dx, dy in direcoes:
        nx, ny = x + dx, y + dy
        # Verifica se a posição está dentro dos limites do tabuleiro
        if 0 <= nx < 7 and 0 <= ny < 7:
            # Verifica se a posição contém uma mina
            if tabela[nx][ny] == "💣":
                minas += 1

    return minas

# Função principal do jogo
def iniciar_jogo():
    while True:
        try:
            # Abre o arquivo de informações pessoais e lê o conteúdo
            arquivo = open("informacaoPessoal.txt", "r")
            lista = arquivo.readlines()
            arquivo.close()

            # Solicita o nome do jogador e adiciona ao arquivo
            nome = input("Digite seu nome: > ")
            lista.append(nome + "\n")

            # Reabre o arquivo no modo de escrita e salva o nome do jogador
            arquivo = open("informacaoPessoal.txt", "w")
            arquivo.writelines(lista)
            arquivo.close()
            break
        except FileNotFoundError:
            # Cria um novo arquivo se ele não for encontrado
            print("Arquivo não encontrado. Criando novo arquivo.")
            arquivo = open("informacaoPessoal.txt", "w")
            arquivo.write("")
            arquivo.close()
        except ValueError:
            print("[ERROR] Valor digitado inválido")

    # Gera o tabuleiro com minas e o tabuleiro visível para o jogador
    tabela_criada = tabela()
    gerar_minas(tabela_criada)
    tabela_visivel = tabela()

    score = 0
    while True:
        mostrar_tabela(tabela_visivel)
        try:
            # Solicita as coordenadas da posição escolhida pelo jogador
            posicaoX = int(input("Digite a posicao X (0 a 6): "))
            posicaoY = int(input("Digite a posicao Y (0 a 6): "))
        except ValueError:
            print("[ERROR] valor digitado inválido :( ")
            continue

        # Verifica se as coordenadas estão dentro dos limites do tabuleiro
        if posicaoX < 0 or posicaoX > 6 or posicaoY < 0 or posicaoY > 6:
            print("\nDigite um número entre os intervalos pedidos\n")
            continue

        # Verifica se a posição contém uma mina
        if tabela_criada[posicaoX][posicaoY] == "💣":
            tabela_visivel[posicaoX][posicaoY] = "💣"
            mostrar_tabela(tabela_visivel)
            print("Infelizmente você perdeu! MINA ENCONTRADA 💣 ")
            # Salva o score do jogador no arquivo
            arquivo = open("informacaoPessoal.txt", "a")
            arquivo.writelines(f"{nome} : {score}\n")
            arquivo.close()
            break
        else:
            # Conta o número de minas ao redor e atualiza o tabuleiro visível
            minas_ao_redor = contar_minas_ao_redor(tabela_criada, posicaoX, posicaoY)
            tabela_visivel[posicaoX][posicaoY] = str(minas_ao_redor)
            score += 1

def main():
    iniciar_jogo()

main()
