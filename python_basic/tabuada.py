valor = int(input("Digite um número para ver a tabuada: "))
while valor == 0 or valor < 0:
    print("O número deve ser maior ou igual a zero. Tente novamente.")
    valor = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    resultado = valor * i
    print(f"{valor} x {i} = {resultado}")
    
