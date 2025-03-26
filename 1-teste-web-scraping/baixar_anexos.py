import requests
from bs4 import BeautifulSoup as bs
import os
from zipfile import ZipFile as zp

diretorio = "1-teste-web-scraping"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0" }

#captura do html
site = requests.get("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos", headers=headers)

site_dados = bs(site.text, "html.parser")

topicos = site_dados.find_all('a', class_="internal-link")

for link in topicos:
    texto = link.get_text(strip=True)  # texto tag <a>
    if texto in ["Anexo I.", "Anexo II."]:
        pdf_url = link['href']  #URL do PDF

        if pdf_url.startswith("/"): #prevenir links relativos
            pdf_url = "https://www.gov.br" + pdf_url

        print(f"Baixando {texto}: {pdf_url}")

        pdf_response = requests.get(pdf_url, headers=headers)
        if pdf_response.status_code == 200:
            nome_arquivo = os.path.join(diretorio, texto.replace(" ", "_").replace(".", "") + ".pdf")
            with open(nome_arquivo, 'wb') as file:
                file.write(pdf_response.content)
            print(f"{nome_arquivo} baixado com sucesso!")
        else:
            print(f"Erro ao baixar {texto}: {pdf_response.status_code}")

#compactando os anexos
zip_path = os.path.join(diretorio, "anexos_compactados.zip")

with zp(zip_path, "w") as zip:
    zip.write(os.path.join(diretorio, "Anexo_I.pdf"), "Anexo_I.pdf")
    zip.write(os.path.join(diretorio, "Anexo_II.pdf"), "Anexo_II.pdf")