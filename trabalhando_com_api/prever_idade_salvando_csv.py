import requests
import csv

def obter_idade(nome):
    url = f"https://api.agify.io?name={nome}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        return {
            "nome": nome,
            "idade": dados.get("age"),
            "contagem": dados.get("count")
        }
    else:
        return {"nome": nome, "erro": "Erro ao acessar a API"}

nomes = input("Digite os nomes separados por vírgula: ").split(",")
nomes = [nome.strip() for nome in nomes]  # Remove espaços em branco

resultados = []

for nome in nomes:
    resultado = obter_idade(nome)
    resultados.append(resultado)

with open("idades.csv", mode="w", newline="", encoding="utf-8") as arquivo_csv:
    campos = ["nome", "idade", "contagem"]
    escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(resultados)

print("Dados salvos em idades.csv")