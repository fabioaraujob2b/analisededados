#pip install requests caso não tenha a biblioteca instalada
# Este código usa a API Agify para prever a idade média de uma pessoa com base no nome fornecido.
import requests

def idade_por_nome(nome):
    url = f"https://api.agify.io?name={nome}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        idade = dados.get('age')
        contagem = dados.get('count')

        if idade is not None and contagem is not None:
            print(f"A idade média para o nome '{nome}' é {idade} anos com base em {contagem} pessoas.")
        else:
            print(f"Não foi possível encontrar dados para o nome '{nome}'.")
    else:
        print(f"Erro ao acessar a API: {resposta.status_code}")        

idade_por_nome(input("Digite um nome: "))

