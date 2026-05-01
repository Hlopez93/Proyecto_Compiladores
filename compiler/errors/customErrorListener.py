from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        token = offendingSymbol.text if offendingSymbol else "EOF"
        
        raise Exception(
            f"[Error Sintáctico] Línea {line}, Columna {column}: "
            f"Error cerca de '{token}'. {msg}"
        )