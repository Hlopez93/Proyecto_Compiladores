from antlr4 import *
from ExpresionesLexer import ExpresionesLexer
from ExpresionesParser import ExpresionesParser

from visitorInterprete import InterpreterVisitor
from visitorSemantico import SemanticVisitor

def ejecutar_archivo(nombre):

    input_stream = FileStream(nombre)

    # ----------- LEXER -----------
    lexer = ExpresionesLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # ----------- PARSER -----------
    parser = ExpresionesParser(stream)
    tree = parser.root()

    # DETENER SI HAY ERRORES SINTÁCTICOS
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Errores sintácticos encontrados. Ejecución detenida.")
        return

    # ----------- SEMÁNTICO -----------
    semantico = SemanticVisitor()
    try:
        semantico.visit(tree)
    except Exception as e:
        print("Error semántico:", e)
        return

    # ----------- INTÉRPRETE -----------
    visitor = InterpreterVisitor(semantico.tabla)
    visitor.visit(tree)

    print("Resultado final variables:")
    print(visitor.memory)


if __name__ == "__main__":
    ejecutar_archivo("programa.txt")