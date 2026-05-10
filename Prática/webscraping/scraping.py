import requests
from bs4 import BeautifulSoup

# 1. Faz a requisição
url = "https://books.toscrape.com/"
response = requests.get(url)

# 2. Parseia o HTML
soup = BeautifulSoup(response.text, "html.parser")

# 3. Extrai os dados
livros = soup.find_all("article", class_="product_pod")

for livro in livros:
    titulo = livro.find("h3").find("a")["title"]
    preco = livro.find("p", class_="price_color").text
    print(f"{titulo} — {preco}")