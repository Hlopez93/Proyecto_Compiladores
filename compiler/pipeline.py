from antlr4 import *
import time

from compiler.gramatica_v3Lexer import gramatica_v3Lexer
from compiler.gramatica_v3Parser import gramatica_v3Parser

from compiler.semantic.visitorSemantico import SemanticVisitor
from compiler.interpreter.visitorInterprete import InterpreterVisitor
from compiler.tac.tac_generator import TACGenerator
from compiler.ir.ir_generator import IRGenerator
from compiler.errors.customErrorListener import CustomErrorListener

def ejecutar_codigo(codigo: str):
    resultado = {
        "fases": [],
        "error": None,
        "tac": "",
        "ir": "",
        "output": ""
    }

    try:
        # LEXER
        start = time.time()

        input_stream = InputStream(codigo)
        lexer = gramatica_v3Lexer(input_stream)
        tokens = CommonTokenStream(lexer)

        tiempo = (time.time() - start) * 1000
        resultado["fases"].append(("Lexer", "OK", round(tiempo, 2)))

        # PARSER
        start = time.time()

        parser = gramatica_v3Parser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(CustomErrorListener())

        tree = parser.root()

        if parser.getNumberOfSyntaxErrors() > 0:
            raise Exception("Errores sintácticos")

        tiempo = (time.time() - start) * 1000
        resultado["fases"].append(("Parser", "OK", round(tiempo, 2)))

        # SEMÁNTICO
        start = time.time()

        sem = SemanticVisitor()
        sem.visit(tree)

        tiempo = (time.time() - start) * 1000
        resultado["fases"].append(("Semántico", "OK", round(tiempo, 2)))

        # TAC
        start = time.time()

        tac = TACGenerator()
        tac.visit(tree)

        tac_code = "\n".join(tac.code)
        resultado["tac"] = tac_code

        # Guarda archivo TAC
        with open("output.tac", "w") as f:
            f.write(tac_code)

        tiempo = (time.time() - start) * 1000
        resultado["fases"].append(("TAC", "OK", round(tiempo, 2)))

        # LLVM IR
        start = time.time()

        irgen = IRGenerator()
        irgen.visit(tree)

        ir_code = str(irgen.module)
        resultado["ir"] = ir_code

        # Guarda archivo LLVM IR
        with open("output.ll", "w") as f:
            f.write(ir_code)

        tiempo = (time.time() - start) * 1000
        resultado["fases"].append(("LLVM IR", "OK", round(tiempo, 2)))

        # INTERPRETE
        start = time.time()

        import io, sys
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

# MODO SCRIPT
if __name__ == "__main__":

    with open("tests/programa.txt", "r", encoding="utf-8") as f:
        codigo = f.read()

    resultado = ejecutar_codigo(codigo)

    print("\n=== FASES ===")
    for f in resultado["fases"]:
        print(f"{f[0]}: {f[1]} ({f[2]} ms)")

    if resultado["error"]:
        print("\n ERROR:")
        print(resultado["error"])
    else:
        print("\n=== OUTPUT ===")
        print(resultado["output"])

        print("\n Archivos generados:")
        print(" - output.tac")
        print(" - output.ll")