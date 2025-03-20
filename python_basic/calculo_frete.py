valor_compra = float(input('Digite o valor da compra: '))

if valor_compra > 0 and valor_compra < 200:
    frete = 10
elif valor_compra > 200 and valor_compra < 500:
    frete = 30
else:
    frete = 50
valor_final = valor_compra + frete
print(f"O valor final da compra é R$ {valor_compra:.2f} + R$ {frete:.2f} de frete = R$ {valor_final:.2f}")
