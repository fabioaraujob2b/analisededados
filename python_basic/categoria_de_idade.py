while True:
    idade = int(input("Digite a idade: "))
    if idade < 0:
        print("Digite um valor positivo")
    else:
        break

if idade > 0 and idade <= 12:
    print("Você é uma criança")
elif idade > 12 and idade <= 18:
    print("Você é um adolescente")
elif idade > 18 and idade <= 60:
    print("Você é um adulto")
else:
    print("Você é um idoso")