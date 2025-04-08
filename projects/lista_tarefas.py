tarefas = []
while True:
    print("\nGerenciador de tarefas")
    print("1 - Adicionar Tarefa")
    print("2 - Remover Tarefa")
    print("3 - Listar Tarefas")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada!")
    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa para remover!")
        else:
            print("\nLista de Tarefas:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")
            try:
                num = int(input("Digite o número da tarefa para remover: ")) - 1
                if 0 <= num < len(tarefas):
                    removida = tarefas.pop(num)
                    print(f"Tarefa '{removida}' removida!")
                else:
                    print("Número inválido!")
            except ValueError:
                print("Digite um número válido!")
        input("\nPressione Enter para continuar...")
    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa adicionada.")
        else:
            print("\nLista de Tarefas:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")
        input("\nPressione Enter para continuar...")
    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")
        input("\nPressione Enter para continuar...")