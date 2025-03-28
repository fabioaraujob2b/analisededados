valor_compra = float(input('Digite o valor da compra: '))
if valor_compra >= 500:
    desconto = valor_compra * 0.10
    imposto = valor_compra * 0.05
    valor_final = valor_compra - desconto + imposto
    print(f'Valor da compra: R$ {valor_compra:.2f}')
    print(f'Desconto: R$ {desconto:.2f}')
else:
    print(f'Valor da compra: R$ {valor_compra:.2f}')