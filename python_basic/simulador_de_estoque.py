#Objetivo desse script é simular um estoque de produtos, onde o usuário pode adicionar, remover, listar e alterar produtos.    
#FAZER DEPOIS
produto = []
quantidade = []
preco = []

while True:
    print("\n1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar produtos")
    print("4 - Alterar produto")
    print("5 - Sair")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        nome = input("Digite o nome do produto: ")
        produto.append(nome)
        qtd = int(input("Digite a quantidade: "))
        quantidade.append(qtd)
        p = float(input("Digite o preço: "))
        preco.append(p)
        print("Produto adicionado com sucesso!")
    elif opcao == 2:
        if len(produto) == 0:
            print("Não há produtos cadastrados.")
        else:
            for i in range(len(produto)):
                print(f"{i + 1} - {produto[i]}")
            indice = int(input("Digite o número do produto que deseja remover: "))
            produto.pop(indice - 1)
            quantidade.pop(indice - 1)
            preco.pop(indice - 1)
            print("Produto removido com sucesso!")
    elif opcao == 3:
        if len(produto) == 0:
            print("Não há produtos cadastrados.")
        else:
            print("Produtos cadastrados:")
            for i in range(len(produto)):
                print(f"Nome: {produto[i]} - Quantidade: {quantidade[i]} - Preço: R${preco[i]}")
    elif opcao == 4:
        if len(produto) == 0:
            print("Não há produtos cadastrados.")
        else:
            for i in range(len(produto)):
                print(f"{i + 1} - {produto[i]}")
            indice = int(input("Digite o número do produto que deseja alterar: "))
            nome = input("Digite o nome do produto: ")
            produto[indice - 1] = nome
            qtd = int(input("Digite a quantidade: "))
            quantidade[indice - 1] = qtd
            p = float(input("Digite o preço: "))
            preco[indice - 1] = p
            print("Produto alterado com sucesso!")
    elif opcao == 5:
        break
    else:
        print("Opção inválida. Digite novamente.")