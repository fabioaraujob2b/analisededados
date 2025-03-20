# Descrição: Este programa recebe 3 notas de um aluno e calcula a média final.
# sum() soma todos os elementos de uma lista.
# len() retorna o número de elementos de uma lista.
# O cálculo da média é feito dividindo a soma das notas pelo número de notas.

notas = []
for i in range(3):
    while True:
        nota = float(input(f"Digite a nota {i + 1}: "))
        if nota > 0:
         notas.append(nota)
         break
        else:
            print("A nota deve ser maior que 0. Digite novamente.")

media = sum(notas) / len(notas)
if media >= 9:
   print(f"Nota A média final {media:.2f}")
elif media >= 7:
    print(f"Nota B média final {media:.2f}")	
elif media >= 5 and media < 7:
    print(f"Nota C média final {media:.2f}")
elif media >= 4:
    print(f"Nota D média final {media:.2f}")
else:
    print(f"Nota F média final {media:.2f}")