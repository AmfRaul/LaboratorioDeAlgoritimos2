2#Uma lista de compras o produto sera a chave e a quantidade que sera comprada o valor
def inserir_item(lista_compras):
    nome = input('Digite o item da compra: ')
    quantidade = int(input('Quantidade do produto: '))

    if nome in lista_compras:
        lista_compras[nome] += quantidade
    else:
        lista_compras[nome] = quantidade 

    return lista_compras


def removerProduto(lista_compras):
    removerProduto = input('Produto a retirar: ')
    if removerProduto in lista_compras:
        del lista_compras[removerProduto]
    else:
        print('Produto não encontrado')

    return lista_compras


def alterarQuantidade(lista_compras):
    produtoAlterar = input('Produto para alterar: ')
    quantidadeAlterada = int(input('Nova quantidade: '))
    if produtoAlterar in lista_compras:
        lista_compras[produtoAlterar] = quantidadeAlterada
    else:
        print("Produto não encontrado")
    return lista_compras

def verLista(lista_compras):
    print('Lista de Compras:')
    for produto, quantidade in lista_compras.items():
        print(f'{produto}: {quantidade}')

def main():
    opc = -1
    lista_compras = {}
    while opc != 0:
        opc = int(input('Coloque a opcao desejada: '))
        if opc == 1:
            inserir_item(lista_compras)
        elif opc == 2:
            removerProduto(lista_compras)
        elif opc == 3:
            alterarQuantidade(lista_compras)
        elif opc == 4:
            verLista(lista_compras)

        else:
            break


main()



