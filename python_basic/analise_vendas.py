valor_compar = float(input("Digite o valor da compra: "))

if valor_compar >= 500:
    desc = valor_compar * 0.5
elif valor_compar >= 1000:
    desc = valor_compar * 1.0
else:
    desc = 0
print(f"O valor da compra é R$ {valor_compar:.2f} e o desconto é R$ {desc:.2f}")