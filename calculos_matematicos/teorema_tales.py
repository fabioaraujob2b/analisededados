def teorema_tales_segmentos(ab, bc, de):
    return (de * bc) / ab
def teorema_tales_triangulos(ad, ab, ae, ac):
    return ad / ab == ae / ac

ef = teorema_tales_segmentos(int(input("Digite o valor de AB: ")), int(input("Digite o valor de BC: ")), int(input("Digite o valor de DE: ")))
print(f'O valor de EF é: {ef} cm')

similar = teorema_tales_triangulos(int(input("Digite o valor de AD: ")), int(input("Digite o valor de AB: ")), int(input("Digite o valor de AE: ")), int(input("Digite o valor de AC: ")))
print(f'Os triângulos são semelhantes? {"Sim" if similar else "Não"}')