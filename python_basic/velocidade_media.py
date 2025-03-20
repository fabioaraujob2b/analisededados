#calcula a velocidade média
distancia = float(input("Digite a distância percorrida (em km): "))
tempo = float(input("Digite o tempo gasto (em horas): "))
vm = distancia / tempo
print(f"A velocidade média é {vm:.2f} km/h")

#calcula o gasto do combustivel
consumo = 12
gasto = distancia / consumo
print(f"O gasto de combustível foi de {gasto:.2f} litros")

