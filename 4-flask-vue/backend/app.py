from flask import Flask, request, jsonify
import pandas as pd


app = Flask(__name__)

# Carregar o CSV
df = pd.read_csv("4-flask-vue\\backend\\Relatorio_cadop.csv", sep=None, engine="python", encoding="utf-8")


def buscar_operadoras(termo):
    """Busca operadoras que contenham o termo na Razao_Social ou Nome_Fantasia."""
    filtro = df[df["Razao_Social"].str.contains(termo, case=False, na=False) |
                df["Nome_Fantasia"].fillna("").str.contains(termo, case=False, na=False)]
    return filtro.to_dict(orient="records")


@app.route("/buscar", methods=["GET"])
def buscar():
    termo = request.args.get("termo", "").strip()
    if not termo:
        return jsonify({"erro": "Informe um termo para buscar."}), 400
    resultado = buscar_operadoras(termo)
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)