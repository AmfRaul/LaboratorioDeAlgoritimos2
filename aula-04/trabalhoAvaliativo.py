
def informar_produtos(armazem):
    nome_produto = input("Produto a incluir: ")
    quantidade_produto = int(input("Quantidade produto: "))
    preço_unitario = float(input("INFORME PREÇO UNITARIO: "))
    armazem[nome_produto] = {
            'quantidade' : quantidade_produto,
            'UnidadePreço' : preço_unitario
        }
    print(armazem)

def buscar_produto(armazem):
    procurar_produto = input("Qual produto deseja procurar: ")
    if procurar_produto in armazem:
        print(f"Produto encontrado{armazem}")
    else:
        print(f"O Produto {procurar_produto} não foi encotrado ")

#Visualizar todos os produtos: Mostre uma lista de todos os produtos disponíveis, juntamente com suas quantidades e preços.


def verProdutos(armazem):
    print(armazem)
    return armazem

#Vender um produto: Solicite o nome do produto vendido e a quantidade vendida.
#Atualize a quantidade em estoque e calcule o valor total da venda.

def venderProdutos(armazem):
    produtoVender = input("Qual produto deseja vender: ")
    quantidadeVender = float(input("Quantidade para venda: "))

    if produtoVender in armazem:
        estoque = armazem[produtoVender]['quantidade']
        if quantidadeVender <= estoque:
            armazem[produtoVender]['quantidade'] -= quantidadeVender

    valorTotalVenda = quantidadeVender * armazem[produtoVender]["UnidadePreço"]
    print("O Valor total das vendas é de R$ ", valorTotalVenda)

    vendasHistorico = [produtoVender, quantidadeVender, valorTotalVenda]
    print("Historico de vendas de", vendasHistorico)

def main()
    armazem = {}
    while True:
        print(" 1- Informar produtos \n 2- Buscar produtos \n 3- Vizualizar todos os produtos \n 4- Vender produto")
        opc = int(input("Digite uma opcao: "))
        if opc == 1:
            informar_produtos(armazem)
        if opc == 2:
            buscar_produto(armazem)
        if opc == 3:
            verProdutos(armazem)
        if opc == 4:
            venderProdutos(armazem)
        if opc == 5:
            break

main()