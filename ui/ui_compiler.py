from flask import Flask, render_template, request, jsonify
from compiler.pipeline import ejecutar_codigo

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/compilar", methods=["POST"])
def compilar():
    try:
        codigo = request.json["codigo"]

        resultado = ejecutar_codigo(codigo)

        return jsonify(resultado)

    except Exception as e:
        return jsonify({
            "error": str(e),
            "fases": [],
            "tac": "",
            "ir": "",
            "output": ""
        })

if __name__ == "__main__":
    app.run(debug=True)