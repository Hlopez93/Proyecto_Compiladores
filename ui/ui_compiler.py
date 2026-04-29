from flask import Flask, render_template, request, jsonify
import time
import io
import sys

from antlr4 import *
from gramatica_v3Lexer import gramatica_v3Lexer
from gramatica_v3Parser import gramatica_v3Parser

from visitorSemantico import SemanticVisitor
from visitorInterprete import InterpreterVisitor
from tac_generator import TACGenerator
from ir_generator import IRGenerator
from customErrorListener import CustomErrorListener

app = Flask(__name__)


def ejecutar_pipeline(codigo):

    resultado = {
        "fases": [],
        "error": None,
        "tac": "",
        "ir": "",
        "output": ""
    }

    try:
        # ========================
        # LEXER
        # ========================
        start = time.time()

        input_stream = InputStream(codigo)
        lexer = gramatica_v3Lexer(input_stream)
        tokens = CommonTokenStream(lexer)

        tiempo = (time.time() - start) * 1000
        resultado["fases"].append(("Lexer", "OK", round(tiempo, 2)))

        # ========================
        # PARSER
        # ========================
        start = time.time()

        parser = gramatica_v3Parser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(CustomErrorListener())

        tree = parser.root()

        if parser.getNumberOfSyntaxErrors() > 0:
            raise Exception("Errores sintácticos")

        tiempo = (time.time() - start) * 1000
        resultado["fases"].append(("Parser", "OK", round(tiempo, 2)))

        # ========================
        # SEMÁNTICO
        # ========================
        start = time.time()

        sem = SemanticVisitor()
        sem.visit(tree)

        tiempo = (time.time() - start) * 1000
        resultado["fases"].append(("Semántico", "OK", round(tiempo, 2)))

        # ========================
        # TAC
        # ========================
        start = time.time()

        tac = TACGenerator()
        tac.visit(tree)
        resultado["tac"] = "\n".join(tac.code)

        tiempo = (time.time() - start) * 1000
        resultado["fases"].append(("TAC", "OK", round(tiempo, 2)))

        # ========================
        # LLVM IR
        # ========================
        start = time.time()

        irgen = IRGenerator()
        irgen.visit(tree)

        resultado["ir"] = str(irgen.module)

        tiempo = (time.time() - start) * 1000
        resultado["fases"].append(("LLVM IR", "OK", round(tiempo, 2)))

        # ========================
        # INTERPRETE
        # ========================
        start = time.time()

        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()

        interpreter = InterpreterVisitor()
        interpreter.visit(tree)

        sys.stdout = old_stdout

        resultado["output"] = mystdout.getvalue()

        tiempo = (time.time() - start) * 1000
        resultado["fases"].append(("Ejecución", "OK", round(tiempo, 2)))

    except Exception as e:
        resultado["error"] = str(e)

    return resultado


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/compilar", methods=["POST"])
def compilar():
    codigo = request.json["codigo"]
    resultado = ejecutar_pipeline(codigo)
    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)