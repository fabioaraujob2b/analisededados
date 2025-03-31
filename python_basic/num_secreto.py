import random
n = int(input("Digite um número de 0 a 99: "))
n_secreto = random.randint(0, 10)
while n >= 0:
    if n == n_secreto:
        print("Você acertou! O número secreto é 7.")
        print("Parabéns! Você ganhou um prêmio!")
        print("Você quer jogar novamente? (s/n)")
        resposta = input().strip().lower()
        if resposta == 's':
            n_secreto = random.randint(0, 10)
            n = int(input("Digite um número de 0 a 9: "))
        else:
            print("Obrigado por jogar!")
        break
    else:
        print("Você errou!")
        n = int(input("Digite um número de 0 a 9: "))