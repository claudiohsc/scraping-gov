import tabula
import pandas as pd
import pdfplumber

anexo1 = "1-teste-web-scraping\Anexo_I.pdf"

#total de páginas do pdf
with pdfplumber.open(anexo1) as pdf:
    total_paginas = len(pdf.pages)

tabelas = tabula.read_pdf(anexo1, pages=f"3-{total_paginas}", multiple_tables=True)

if not tabelas:
    raise ValueError("Nenhuma tabela foi encontrada no PDF.")

# Pegar os nomes das colunas da primeira tabela como referência
colunas_padrao = tabelas[0].columns.tolist()

tabelas_padronizadas = []

for i, tabela in enumerate(tabelas):
    
    tabela = tabela.dropna(axis=1, how="all")

    # remover cabecalhos repetidos nas pags
    if any(col in tabela.columns[0] for col in colunas_padrao):
        tabela = tabela.iloc[1:] 
    
    # Garantir o cabecalho padrao
    tabela = tabela.reindex(columns=colunas_padrao)

    tabelas_padronizadas.append(tabela)

df_final = pd.concat(tabelas_padronizadas, ignore_index=True)

df_final = df_final.rename(columns={"OD":"Seg. Odontológica", "AMB":"Seg. Ambulatorial"})

df_final.to_csv("2-teste-transformacao/tabela_unificada.csv", index=False)

print("Arquivo salvo com sucesso!")
