import locale
# Configuração para exibir valores em reais
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

vh = float(input("Digite o valor da hora: "))
ht = float(input("Digite a quantidade de horas trabalhadas: "))
pd = float(input("Digite o percentual de desconto: "))
sb = ht * vh
td = (pd/100) * sb
sl = sb - td
print(f"O salário líquido é de R$ {locale.format_string('%.2f', sl, grouping=True)}")  
