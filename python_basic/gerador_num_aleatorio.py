import random
import math

# Gerar um número aleatório entre 0 e 100
numero_aleatorio = math.ceil(10 * random.random(1, 100))
print(numero_aleatorio)

#Gera um resultado aleatório dentre uma lista de opções idependete do tipo do dado
opcoes = [1, 2, 3, '4', 5, 6, "7", True, 9, False]
escolha = random.choice(opcoes)
print(escolha)
