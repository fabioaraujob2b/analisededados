altura = float(input('Digite sua altura em metros: '))
sexo = input('Digite seu sexo, sendo M para masculino e F para feminino: ')
if sexo == 'M' or sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
    print(f'Seu peso ideal é {peso_ideal:.2f}')
elif sexo == 'F' or sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é {peso_ideal:.2f}')