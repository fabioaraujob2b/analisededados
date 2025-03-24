import random 

jogador1 = []
jogador2 = []
pontos1 = 0
pontos2 = 0

while True:
    print("Iniciar o jogo")
    print("1 - Jogar")
    print("2 - Placar")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        jogador1 = random.randint(1, 6)
        print(f"Jogador 1: {jogador1}")
        jogador2 = random.randint(1, 6)
        print(f"Jogador 2: {jogador2}")
        if jogador1 > jogador2:
            print("Jogador 1 venceu!")
            pontos1 += 1
        elif jogador2 > jogador1:   
            print("Jogador 2 venceu!")
            pontos2 += 1
        else:
            print("Empate!")
    elif opcao == 2:
        print("Placar:")
        resultado1 = pontos1.count(1)
        resultado2 = pontos2.count(1)
        print(f"Jogador 1: {resultado1}")
        print(f"Jogador 2: {resultado2}")
    elif opcao == 3:
        break1
    else:
        print("Opção inválida. Digite novamente.")            