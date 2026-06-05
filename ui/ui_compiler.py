from flask import Flask, render_template, request, jsonify, send_file
import os

from compiler.pipeline import ejecutar_codigo
from compiler.optimizer.manual_ir_runner import ManualIRRunner

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/compilar", methods=["POST"])
def compilar():
    try:
        codigo = request.json["codigo"]
        passes = request.json.get("passes", [])
        targets = request.json.get(
            "targets",
            ["linux", "windows"]
        )

        resultado = ejecutar_codigo(
            codigo,
            passes,
            targets
        )

        return jsonify(resultado)

    except Exception as e:
        return jsonify({
            "error": str(e),
            "fases": [],
            "tac": "",
            "ir": "",
            "ir_optimizado": "",
            "output": ""
        })

@app.route("/download/manual-ir")
def download_manual_ir():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    file_path = os.path.join(
        BASE_DIR,
        "manual_opt.ll"
    )

    if not os.path.exists(file_path):
        return jsonify({
            "error": "No existe IR manual generado"
        }), 404

    return send_file(
        file_path,
        as_attachment=True,
        download_name="manual_opt.ll"
    )

@app.route("/run-manual-ir")
def run_manual_ir():

    try:

        runner = ManualIRRunner()

        output = runner.run()

        return jsonify({
            "success": True,
            "output": output
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)