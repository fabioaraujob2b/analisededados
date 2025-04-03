nome = []
sexo = []
idade = []

qtd_maiores_idade = 0
qtd_fem = 0

for i in range(5):
    nome.append(input("Digite o nome: "))
    sexo.append(input("Digite 'f' para feminino ou 'm' para masculino: ").lower())
    idade.append(int(input("Informe a idade: ")))

    if i == 0:
        mais_velho = idade[i]
        mais_novo = idade[i]
        nome_velho = nome[i]
        nome_novo = nome[i]
    else:
        if idade[i] > mais_velho:
            mais_velho = idade[i]
            nome_velho = nome[i]
        if idade[i] < mais_novo:
            mais_novo = idade[i]
            nome_novo = nome[i]

    if idade[i] >= 18:
        qtd_maiores_idade += 1
    if sexo[i] == 'f':
        qtd_fem += 1

print(f"\nA quantidade de pessoas maiores de idade é: {qtd_maiores_idade}")
print(f"O nome da pessoa mais nova é: {nome_novo} e tem {mais_novo} anos")
print(f"O nome da pessoa mais velha é: {nome_velho} e tem {mais_velho} anos")
print(f"A quantidade de pessoas do sexo feminino é: {qtd_fem}")
