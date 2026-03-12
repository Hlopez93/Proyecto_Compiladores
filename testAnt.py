from antlr4 import *
from ExpresionesLexer import ExpresionesLexer
from ExpresionesParser import ExpresionesParser
from antlr4.error.ErrorListener import ErrorListener


# Listener personalizado para capturar errores
class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()
        self.errors = 0

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors += 1
        print(f"Error de sintaxis en línea {line}, columna {column}: {msg}")


def analizar(texto):
    input_stream = InputStream(texto)
    lexer = ExpresionesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExpresionesParser(stream)

    # Remover errores por defecto
    parser.removeErrorListeners()
    error_listener = MyErrorListener()
    parser.addErrorListener(error_listener)

    # CAMBIA ESTA REGLA si no se llama prog
    tree = parser.root()

    if error_listener.errors == 0:
        print("Expresión válida")
        print("Árbol:", tree.toStringTree(recog=parser))
    else:
        print("Expresión inválida")


if __name__ == "__main__":
    while True:
        texto = input("\nIngresa una expresión (o 'salir'): ")

        if texto.lower() == "salir":
            print("Finalizando...")
            break

        analizar(texto)