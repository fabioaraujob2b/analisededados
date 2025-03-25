import requests
from import BeautifulSoup4
import pandas as pd

url = "https://books.toscrape.com/"
reponse = requests.get(url)
reponse.encoding = 'utf-8' # Para garantir que a página seja decodificada corretamente
html = reponse.text
soup = BeautifulSoup(html, 'html.parser')

livros = soup.find_all("article", class_="product_pod")

dados = []

for livro in livros:
    titulo = livro.h3.a['title']
    preco = livro.find("p", class_="price_color").text.replace("£", "").strip()
    estoque = livro.find("p", class_="instock availability").text.strip()
    dados.append([titulo, preco, estoque])

df = pd.DataFrame(dados)
print(df)