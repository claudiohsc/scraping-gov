from flask import Flask
import pandas as pd

app = Flask(__name__)

# Carregar o CSV
df = pd.read_csv("Relatorio_cadop.csv", sep=None, engine="python", encoding="utf-8")

def buscar_operadoras(termo):
    """Busca operadoras que contenham o termo na Razao_Social ou Nome_Fantasia."""
    filtro = df[df["Razao_Social"].str.contains(termo, case=False, na=False) |
                df["Nome_Fantasia"].fillna("").str.contains(termo, case=False, na=False)]
    return filtro.to_dict(orient="records")


if __name__ == "__main__":
    app.run(debug=True)