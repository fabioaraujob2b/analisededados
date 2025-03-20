# Estou usando o while para que o usuário não possa digitar uma idade negativa.
while True:
    idade = int(input("Digite a sua idade: "))
    if idade < 0:
        print("Idade inválida. Digite uma idade válida.")
    else:
        break

if idade >= 18 and idade < 100:
    print(f"Você é maior de idade, pois você possui {idade} anos.")
elif idade >= 100:
    print(f"{idade} anos? Tá fazendo hora extra, hein?")
else:
    print(f"Você é menor de idade, pois você tem {idade} anos.")