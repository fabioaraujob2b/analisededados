while True:
    valor_produto = float(input('Digite o valor do produto: '))
    if valor_produto == 0 or valor_produto < 0:
        print('Não é possível calcular o desconto de um produto com valor 0 ou negativo.')
    else:
        break
desconto = 10
valor_desconto = valor_produto * desconto / 100
print(f'O valor do desconto é de R$ {valor_desconto:.2f}')
valor_final = valor_produto - valor_desconto
print(f'O valor final do produto com desconto é de R$ {valor_final:.2f}')
