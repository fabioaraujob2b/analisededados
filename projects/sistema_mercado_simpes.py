import os

produtos = []
precos = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela
    print("\n====== Caixa do Mercado ======")
    print("1. Adicionar Produto")
    print("2. Remover Produto")
    print("3. Listar Produtos")
    print("4. Ver total")
    print("5. Finalizar Compra")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produtos.append(input("Digite o nome do produto: "))
        precos.append(float(input("Digite o preço do produto: ")))
        print(f"Produto '{produtos[-1]}' adicionado com sucesso!")
        input("Produto adicionado! Pressione Enter para continuar...")
    elif opcao == "2":
        if not produtos:
            print("Nenhum produto para remover!")
            input("Pressione Enter para continuar...")
        else:
            print("\nLista de Produtos:")
            for i, produto in enumerate(produtos, start=1):
                print(f"{i}. {produto}")
            try:
                num = int(input("Digite o número do produto para remover: ")) - 1
                if 0 <= num < len(produtos):
                    removido = produtos.pop(num)
                    print(f"Produto '{removido}' removido!")
                else:
                    print("Número inválido!")
            except ValueError:
                print("Digite um número válido!")
            input("\nPressione Enter para continuar...")
    elif opcao == "3":
        if not produtos:
            print("Nenhum produto adicionado.")
        else:
            print("\nLista de Produtos:")
            for i, (produto, preco) in enumerate(zip(produtos, precos), start=1):
                print(f"{i}. {produto} - R$ {preco:.2f}")
        input("\nPressione Enter para continuar...")
    elif opcao == "4":
        soma = sum(precos)
        print(f"Total: R$ {soma:.2f}")
        input("Pressione Enter para continuar...")
    elif opcao == "5":
        if not produtos:
            print("Nenhum produto adicionado.")
        else:
            print("\nLista de Produtos:")
            for i, (produto, preco) in enumerate(zip(produtos, precos), start=1):
                print(f"{i}. {produto} - R$ {preco:.2f}")
            input("Pressione Enter para finalizar a compra...")
            print("Compra finalizada!")
            break
    elif opcao == "6":
        print("Saindo do programa...")
        break