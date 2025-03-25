produto = []
carrinho = []
total = 0

while True:
    print("1 para adicionar produto")
    print("2 para remover produto")
    print("3 para ver carrinho")
    print("4 para finalizar")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade: "))
        produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
        carrinho.append(produto)
        print(f"{quantidade}x {nome} adicionado ao carrinho!")
    elif opcao == 2:
        nome = input("Digite o nome do produto a remover: ")
        for item in carrinho:
            if item["nome"] == nome:
                carrinho.remove(item)
                print(f"{nome} removido do carrinho.")
                break
        else:
            print("Produto não encontrado no carrinho.")
    elif opcao == 3:
        if not carrinho:
            print("Carrinho vazio.")
        else:
            print("\nCarrinho:")
            for item in carrinho:
                print(f"{item['quantidade']}x {item['nome']} - R${item['preco']:.2f} cada")
    elif opcao == 4:
        total = sum(item["preco"] * item["quantidade"] for item in carrinho)
        print(f"Total da compra: R${total:.2f}")
        break
    else:
        print("Opção inválida.")
    