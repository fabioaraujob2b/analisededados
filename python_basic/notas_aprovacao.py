while True:
    nota1 = float(input("Digite a sua nota: "))
    nota2 = float(input("Digite a sua nota: "))
    if nota1 < 0 and nota2 < 0:
        print("Nota inválida. Digite um valor positivo.")
    else:
        break
media = (nota1 + nota2) / 2
if media >= 7:
    print(f"Parabéns! Sua média foi {media:.2f}. Você foi aprovado.")
elif media >= 5 and media < 7:
    print(f"Sua média foi {media:.2f}. Você está de recuperação.")
else:
    print(f"Sua média foi {media:.2f}. Você foi reprovado.")

