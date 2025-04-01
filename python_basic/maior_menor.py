lista = []
for i in range(5):
    n = int(input('Digite um número: '))
    lista.append(n)
minimo = min(lista)
maximo = max(lista)
print(f'O maior número é {maximo} e o menor número é {minimo}.')
print(f'A lista é {lista}.')
print(f'O maior número está na posição {lista.index(maximo)} e o menor número está na posição {lista.index(minimo)}.')