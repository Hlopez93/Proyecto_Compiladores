from antlr4 import *
from gramatica_v3Lexer import gramatica_v3Lexer
from gramatica_v3Parser import gramatica_v3Parser

from compiler.interpreter.visitorInterprete import InterpreterVisitor
from compiler.semantic.visitorSemantico import SemanticVisitor
from compiler.tac.tac_generator import TACGenerator
from compiler.ir.ir_generator import IRGenerator

from compiler.errors.customErrorListener import CustomErrorListener

import time

def ejecutar_archivo(nombre):
    input_stream = FileStream(nombre, encoding='utf-8')

    # ----------- LEXER -----------
    start = time.time()

    lexer = gramatica_v3Lexer(input_stream)
    stream = CommonTokenStream(lexer)

    # ----------- PARSER -----------
    start = time.time()

    parser = gramatica_v3Parser(stream)

    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    tree = parser.root()

    end = time.time()
    print(f"[OK] Parser en {(end - start)*1000:.2f} ms")

    # SE DETIENE SI HAY ERRORES SINTÁCTICOS
    if parser.getNumberOfSyntaxErrors() > 0:
        print(" Errores sintácticos encontrados. Ejecución detenida.")
        return

    # ----------- SEMÁNTICO -----------
    start = time.time()

    semantico = SemanticVisitor()
    try:
        semantico.visit(tree)
    except Exception as e:
        print(" Error semántico:", e)
        return
    
    end = time.time()
    print(f"[OK] Semántico en {(end - start)*1000:.2f} ms")

    # ----------- TAC -----------
    start = time.time()

    tac = TACGenerator()
    tac.visit(tree)

    tac_code = tac.get_code()

    end = time.time()
    print(f"[OK] TAC en {(end - start)*1000:.2f} ms")

    print("\n===== TAC GENERADO =====")
    print(tac_code)

    # Guardar archivo TAC
    with open("output.tac", "w", encoding="utf-8") as f:
        f.write(tac_code)

    # ----------- LLVM IR -----------
    start = time.time()

    irgen = IRGenerator()
    irgen.visit(tree)

    llvm_code = str(irgen.module)

    end = time.time()

    print("\n===== LLVM IR =====")
    print(llvm_code)

    with open("output.ll", "w") as f:
        f.write(llvm_code)

    print(f"[OK] LLVM IR en {(end - start)*1000:.2f} ms")

    # ----------- INTÉRPRETE -----------
    start = time.time()

    interprete = InterpreterVisitor()

    try:
        interprete.visit(tree)
    except Exception as e:
        print(" Error en ejecución:", e)
        return
    
    end = time.time()
    print(f"\n[OK] Ejecución en {(end - start)*1000:.2f} ms")

if __name__ == "__main__":
    ejecutar_archivo("programa.txt")