nomes = []
medias = []
situacoes = []

for i in range(10):
    nome = input(f"Digite o nome do {i+1}.o aluno: ")
    media = float(input(f"Digite a média de {nome}: "))

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    nomes.append(nome)
    medias.append(media)
    situacoes.append(situacao)

print("\nResultado dos alunos: ")
for i in range(10):
    print(f"{nomes[i]} - Média: {medias[i]:.2f} - Situação: {situacoes[i]}")