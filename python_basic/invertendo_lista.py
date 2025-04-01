#Invertendo uma lista sem user .reverse()
# Criando uma lista
lista = [1, 2, 3, 4, 5]
# Criando uma lista vazia
lista_invertida = []
# Percorrendo a lista de trás para frente   
for i in range(len(lista)-1, -1, -1):
    # Adicionando o elemento na lista invertida
    lista_invertida.append(lista[i])
# Imprimindo a lista invertida
print(lista_invertida)
# Invertendo uma lista com user .reverse()
lista_reverser = reversed(lista)
# Imprimindo a lista invertida
print(list(lista_reverser))
# Invertendo uma lista com user [::-1]  
lista_reverser = lista[::-1]
# Imprimindo a lista invertida
print(lista_reverser)
# Invertendo uma lista com user .reverse() e print()
lista.reverse()
# Imprimindo a lista invertida  
print(lista)