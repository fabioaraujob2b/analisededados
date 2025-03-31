import time


while True:
    n = int(input("Digite um número: "))
    if n < 0:
        print("Número inválido!")
        continue
    for i in range(n, 0, -1):
        print("Aguardando...")
        time.sleep(n)
    print("Tempo de espera finalizado!")
    break
        