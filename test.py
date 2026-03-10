from antlr4 import *
from ExpresionesLexer import ExpresionesLexer
from ExpresionesParser import ExpresionesParser
from visorEvaluador import visorEvaluador
from antlr4.error.ErrorListener import ErrorListener

def ejecutar_archivo(nombre):

    input_stream = FileStream(nombre)

    lexer = ExpresionesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExpresionesParser(stream)

    tree = parser.root()

    visitor = visorEvaluador()
    visitor.visit(tree)

    print("Resultado final variables:")
    print(visitor.memory)


if __name__ == "__main__":

    ejecutar_archivo("programa.txt")