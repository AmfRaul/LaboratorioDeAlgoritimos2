from jogo_campoMinado import pontuacoes, iniciar_jogo

def menu():
    while True:
        try:
            print("1 - Iniciar novo jogo")
            print("2 - Ver score")
            print("3 - Minhas pontuações")
            print("4 - Sair")
            opc = int(input("Digite a opção desejada: "))
            if opc == 1:
                iniciar_jogo()
            elif opc == 2:
                #ver_score()
                pass
            elif opc == 3:
                pontuacoes()
            elif opc == 4:
                print("<< Até Mais >>")
                break
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("[ERROR] valor digitado não é valido")
def main():
    menu()

main()
