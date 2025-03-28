valor1 = float(input("Digite o primeiro valor: "))
while valor1 == 0:  
    print("O primeiro valor não pode ser zero. Tente novamente.")
    valor1 = float(input("Digite o primeiro valor: "))

valor2 = float(input("Digite o segundo valor: "))
while valor2 == 0:
    print("O segundo valor não pode ser zero. Tente novamente.")
    valor2 = float(input("Digite o segundo valor: "))
resultado = valor1 / valor2
print(f"O resultado da divisão é: {resultado:.2f}")