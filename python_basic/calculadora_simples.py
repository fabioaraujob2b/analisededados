#Calculadora simples de 2 números
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

#Valida a operação
#Se o usuário digitar algo diferente de +, -, *, /, ele pede para digitar novamente
while op not in ["+", "-", "*", "/"]:
    op = input("Operação inválida! Digite a operação (+, -, *, /): ")
if op == "+":
    print("Resultado: ", n1 + n2)
elif op == "-":
    print("Resultado: ", n1 - n2)
elif op == "*":
    print("Resultado: ", n1 * n2)
elif op == "/":
    print("Resultado: ", n1 / n2)
else:
    print("Operação inválida!")