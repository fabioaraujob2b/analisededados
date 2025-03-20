# Descrição: Programa que calcula a idade de uma pessoa a partir do ano de nascimento.  
ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
resultado = ano_atual - ano_nascimento
print(f'A idade é {resultado} anos')