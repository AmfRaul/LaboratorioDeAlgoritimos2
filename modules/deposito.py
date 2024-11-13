def depositar_dinheiro(depos):
    try:
        while True:
            arquivo = open("modules/banco.txt", "r+")
            extrato = open("modules/extrato.txt", "a")

            lista_extrato = extrato.readlines()
            lista = arquivo.readlines()
            lista += depos
            lista_extrato.append(depos)

            arquivo.close
            extrato.close
            return depos
        
    except ValueError:
        print("[ERROR] valor informado incorreto")