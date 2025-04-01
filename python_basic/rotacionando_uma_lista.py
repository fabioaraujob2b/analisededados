#Rotacionando uma lista n posições para a direita
lista = [1, 2, 3, 4, 5]
print(f"Lista original: {lista}")
n = 2
n = n % len(lista)
lista = lista[-n:] + lista[:-n]
print(f"Lista rotacionada: {lista}")  