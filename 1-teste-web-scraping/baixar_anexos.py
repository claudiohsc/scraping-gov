import requests
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0" }

#captura do html
site = requests.get("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos", headers=headers)

site_dados = bs(site.text, "html.parser")

topicos = site_dados.find_all('a', class_="internal-link")

