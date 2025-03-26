import tabula
import pandas as pd

anexo1 = "1-teste-web-scraping\Anexo_I.pdf"

tabelas = tabula.read_pdf(anexo1, pages="3-181", multiple_tables=True)

tabelas_limpa = []

colunas_cabecalho = ["PROCEDIMENTO", "RN\n(alteração)","VIGÊNCIA","OD", "AMB", "HCO", "REF", "PAC", "DUT", "SUBGRUPO" "GRUPO", "CAPÍTULO"]

for tabela in tabelas:
    if any(col in tabela.columns[0] for col in colunas_cabecalho):
        tabela = tabela.iloc[1:]  # Remove a primeira linha se for cabeçalho

    tabelas_limpa.append(tabela)

# Concatenando todas as tabelas limpas
df_final = pd.concat(tabelas_limpa, ignore_index=True)

df_final.to_csv("2-teste-transformacao/tabela_unificada.csv", index=False)
