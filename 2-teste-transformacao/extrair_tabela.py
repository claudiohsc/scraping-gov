import tabula

anexo1 = "1-teste-web-scraping\Anexo_I.pdf"

tabelas = tabula.read_pdf(anexo1, pages="3")

print(tabelas)