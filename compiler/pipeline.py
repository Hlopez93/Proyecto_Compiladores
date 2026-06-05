from antlr4 import *
import time

from compiler.gramatica_v4Lexer import gramatica_v4Lexer
from compiler.gramatica_v4Parser import gramatica_v4Parser

from compiler.semantic.visitorSemantico import SemanticVisitor
from compiler.interpreter.visitorInterprete import InterpreterVisitor

from compiler.tac.tac_generator import TACGenerator
from compiler.ir.ir_generator import IRGenerator

from compiler.optimizer.manual_optimizer import LLVMManualOptimizer
from compiler.diff.ir_diff import generate_diff

from compiler.codegen.native_generator import NativeGenerator

from compiler.errors.customErrorListener import CustomErrorListener


def ejecutar_codigo(codigo: str, manual_passes=None, targets=None):

    if manual_passes is None:
        manual_passes = []

    if targets is None:
        targets = ["linux", "windows"]

    resultado = {
        "fases": [],
        "error": None,
        "tac": "",
        "ir": "",
        "ir_manual": "",
        "diff": [],
        "ejecutables": {},
        "output": ""
    }

    try:

        # ==================================================
        # LEXER
        # ==================================================
        start = time.time()

        input_stream = InputStream(codigo)

        lexer = gramatica_v4Lexer(input_stream)

        tokens = CommonTokenStream(lexer)

        tiempo = (time.time() - start) * 1000

        resultado["fases"].append(
            ("Lexer", "OK", round(tiempo, 2))
        )

        # ==================================================
        # PARSER
        # ==================================================
        start = time.time()

        parser = gramatica_v4Parser(tokens)

        parser.removeErrorListeners()
        parser.addErrorListener(CustomErrorListener())

        tree = parser.root()

        if parser.getNumberOfSyntaxErrors() > 0:
            raise Exception("Errores sintácticos")

        tiempo = (time.time() - start) * 1000

        resultado["fases"].append(
            ("Parser", "OK", round(tiempo, 2))
        )

        # ==================================================
        # SEMÁNTICO
        # ==================================================
        start = time.time()

        sem = SemanticVisitor()
        sem.visit(tree)

        tiempo = (time.time() - start) * 1000

        resultado["fases"].append(
            ("Semántico", "OK", round(tiempo, 2))
        )

        # ==================================================
        # TAC
        # ==================================================
        start = time.time()

        tac = TACGenerator()
        tac.visit(tree)

        tac_code = "\n".join(tac.code)

        resultado["tac"] = tac_code

        with open("output.tac", "w", encoding="utf-8") as f:
            f.write(tac_code)

        tiempo = (time.time() - start) * 1000

        resultado["fases"].append(
            ("TAC", "OK", round(tiempo, 2))
        )

        # ==================================================
        # LLVM IR
        # ==================================================
        start = time.time()

        irgen = IRGenerator()
        irgen.visit(tree)

        ir_code = str(irgen.module)

        resultado["ir"] = ir_code

        with open("output.ll", "w", encoding="utf-8") as f:
            f.write(ir_code)

        tiempo = (time.time() - start) * 1000

        resultado["fases"].append(
            ("LLVM IR", "OK", round(tiempo, 2))
        )

        # ==================================================
        # OPTIMIZACIÓN MANUAL
        # ==================================================
        start = time.time()

        if manual_passes:

            manual_optimizer = LLVMManualOptimizer()

            manual_ir = manual_optimizer.optimize(
                "output.ll",
                manual_passes
            )

            resultado["ir_manual"] = manual_ir

            ir_para_compilar = "manual_opt.ll"

            tiempo = (time.time() - start) * 1000

            resultado["fases"].append(
                (
                    "Optimización Manual",
                    "OK",
                    round(tiempo, 2)
                )
            )

        else:

            resultado["ir_manual"] = ir_code

            ir_para_compilar = "output.ll"

        # ==================================================
        # DIFF VIEWER
        # ==================================================
        resultado["diff"] = generate_diff(
            resultado["ir"],
            resultado["ir_manual"]
        )

        # ==================================================
        # GENERACIÓN CÓDIGO NATIVO
        # ==================================================
        start = time.time()

        native = NativeGenerator(
            optimized_ir=ir_para_compilar
        )

        resultado["ejecutables"] = native.generate_all(
            targets
        )

        tiempo = (time.time() - start) * 1000

        resultado["fases"].append(
            (
                "Código Nativo",
                "OK",
                round(tiempo, 2)
            )
        )

        # ==================================================
        # INTERPRETE
        # ==================================================
        start = time.time()

        import io
        import sys

        old_stdout = sys.stdout

        sys.stdout = mystdout = io.StringIO()

        interpreter = InterpreterVisitor()
        interpreter.visit(tree)

        sys.stdout = old_stdout

        resultado["output"] = mystdout.getvalue()

        tiempo = (time.time() - start) * 1000

        resultado["fases"].append(
            (
                "Ejecución",
                "OK",
                round(tiempo, 2)
            )
        )

    except Exception as e:

        resultado["error"] = str(e)

    return resultado


if __name__ == "__main__":

    with open(
        "tests/programa.txt",
        "r",
        encoding="utf-8"
    ) as f:
        codigo = f.read()

    resultado = ejecutar_codigo(codigo)

    print("\n=== FASES ===")

    for fase in resultado["fases"]:
        print(
            f"{fase[0]}: {fase[1]} ({fase[2]} ms)"
        )

    if resultado["error"]:

        print("\nERROR:")
        print(resultado["error"])

    else:

        print("\n=== OUTPUT ===")
        print(resultado["output"])

        print("\nArchivos generados:")
        print(" - output.tac")
        print(" - output.ll")

        if resultado["ir_manual"]:
            print(" - manual_opt.ll")