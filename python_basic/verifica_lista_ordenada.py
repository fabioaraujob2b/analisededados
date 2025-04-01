lista = [1, 2, 3, 4, 5, -2]
for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        print("A lista não está ordenada.")
        break
else:
    print("A lista está ordenada.")
