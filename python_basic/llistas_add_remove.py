#Programa para adicionar, remover e manipular uma lista de números inteiros
# Este programa permite ao usuário adicionar, remover e manipular uma lista de números inteiros.

import os

lista = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela
    print("------- MENU -------")
    print("1. Adicionar item")
    print("2. Ver lista")
    print("3. Remover item")
    print("4. Ver posição de um número (índice)")
    print("5. Ordernar lista")
    print("6. Inverter a lista")
    print("7. Limpar lista")
    print("8. Inserir número em posição específica")
    print("9. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        num = int(input("Digite um número para adicionar à lista: "))
        lista.append(num)
        input("Número adicionado! Pressione Enter para continuar...")
    elif opcao == 2:
        print("Lista atual: ", lista)
        input("Pressione Enter para continuar...")
    elif opcao == 3:
        if not lista:
            print("A lista está vazia!")
            input("Pressione Enter para continuar...")
        else:
            num = int(input("Digite o número que deseja remover: "))
            if num in lista:
                lista.remove(num)
                print(f"Número {num} removido!")
            else:
                print(f"Número {num} não encontrado na lista.")
        input("Pressione Enter para continuar...")
    elif opcao == 4:
        num = int(input("Digite o número que deseja encontrar: "))
        if num in lista:
            print(f"Posição: {lista.index(num)}")
        else:
            print(f"Número {num} não encontrado na lista.")
        input("Pressione Enter para continuar...")
    elif opcao == 5:
        lista.sort()
        print("Lista ordenada!")
        input("Pressione Enter para continuar...")
    elif opcao == 6:
        lista.reverse()
        print("Lista invertida!")
        input("Pressione Enter para continuar...")
    elif opcao == 7:
        lista.clear()
        print("Lista limpa!")
        input("Pressione Enter para continuar...")
    elif opcao == 8:
        num = int(input("Digite um número para adicionar à lista: "))
        pos = int(input("Digite a posição onde deseja adicionar o número: "))
        if 0 <= pos <= len(lista):
            lista.insert(pos, num)
            print(f"Número {num} adicionado na posição {pos}!")
        else:
            print("Posição inválida!")
        input("Pressione Enter para continuar...")
    elif opcao == 9:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")
        input("Pressione Enter para continuar...")
