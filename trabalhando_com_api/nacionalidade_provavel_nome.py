#Esse programa usa a API do Nationalize.io
import requests
import csv

def obter_nacionalidade(nome):
    url = f"https://api.nationalize.io?name={nome}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        paises = dados.get('country', [])
        
        if paises:
            pais_mais_provavel = max(paises, key=lambda p: p.get('probability', 0))
            return {
                "nome": nome,
                "pais": pais_mais_provavel.get('country_id', "Desconhecido"),
                "probabilidade": round(pais_mais_provavel.get('probability', 0), 2)
            }
        else:
            return {
                "nome": nome,
                "pais": "Desconhecido",
                "probabilidade": 0.0
            }
    else:
        return {
            "nome": nome,
            "pais": "Erro na requisição",
            "probabilidade": 0.0
        }

nomes = input("Digite os nomes separados por vírgula: ").split(",")
nomes = [nome.strip() for nome in nomes if nome.strip()]
resultados = []

for nome in nomes:
    info = obter_nacionalidade(nome)
    resultados.append(info)

with open('nacionalidade.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    campos = ['nome', 'pais', 'probabilidade']
    escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(resultados)

for pessoa in resultados:
    print(f"Nome: {pessoa['nome']}, País: {pessoa['pais']}, Probabilidade: {pessoa['probabilidade']:.2f}")