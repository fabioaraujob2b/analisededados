# Descrição: Este programa recebe 3 valores e verifica se é possível formar um triângulo com esses valores. Caso seja possível, o programa informa o tipo de triângulo formado (equilátero, isósceles ou escaleno).
#append() - Adiciona um item ao final da lista.
lados = []
for i in range(3):
    while True:
        lado = float(input(f"Digite o lado {i + 1} do triângulo: "))    
        if lado > 0:
            lados.append(lado)  
            break
        else:
            print("O lado do triângulo deve ser maior que 0. Digite novamente.")

a, b, c = lados
if a == b == c:
    print("Triângulo equilátero")
elif a == b or a == c or b == c:
    print("Triângulo isósceles")
elif a != b != c:
    print("Triângulo escaleno")   