from flask import Flask, request, jsonify, send_from_directory
import pandas as pd


app = Flask(__name__, static_folder="../frontend")

# Carregar o CSV
df = pd.read_csv("4-flask-vue\\backend\\Relatorio_cadop.csv", sep=None, engine="python", encoding="utf-8")


def buscar_operadoras(termo):
    """Busca operadoras que contenham o termo na Razao_Social ou Nome_Fantasia."""
    
    termo = termo.strip()
    if not termo:
        return [{"erro": "Informe um termo válido para a busca."}]
    
    # Realiza a busca no DataFrame
    filtro = df[df["Razao_Social"].str.contains(termo, case=False, na=False) |
                df["Nome_Fantasia"].str.contains(termo, case=False, na=False)]
    
    filtro = filtro.fillna("Não informado")
    
    colunas_relevantes = [
        'Razao_Social', 'Nome_Fantasia', 'CNPJ', 'DDD', 'Telefone', 
        'Endereco_eletronico', 'Cidade', 'UF'
    ]
    
    # Filtra apenas as colunas relevantes
    colunas_existentes = [col for col in colunas_relevantes if col in filtro.columns]
    filtro_relevante = filtro[colunas_existentes]
    
    if filtro_relevante.empty:
        return [{"erro": "Nenhuma operadora encontrada."}]
    
    return filtro_relevante.to_dict(orient="records")



@app.route("/buscar", methods=["GET"])
def buscar():
    termo = request.args.get("termo", "").strip()
    if not termo:
        return jsonify({"erro": "Informe um termo para buscar."}), 400
    resultado = buscar_operadoras(termo)
    return jsonify(resultado)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(debug=True)
