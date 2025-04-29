import math
#A pílha de chamada com recursão
def fat(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fat(x - 1)

while True:
    try:
        valor = int(input("Digite um número inteiro positivo: "))
        if valor < 0:
            print("Número inválido!")
        elif valor > 999:
            print("Valor muito grande!")
        else:
            break
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")
    
fatorial = fat(valor)
if fatorial > 10**6:  # Exibir como exponenciação se o valor for muito grande
    base = fatorial / (10 ** int(math.log10(fatorial)))
    expoente = int(math.log10(fatorial))
    print(f"O fatorial de {valor} é aproximadamente {base:.2f}e{expoente}")
else:
    print(f"O fatorial de {valor} é {fatorial}")