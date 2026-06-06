from compiler.gramatica_v4Visitor import gramatica_v4Visitor
from compiler.semantic.tablaSimbolos import TablaSimbolos

# EXCEPCIONES DE CONTROL
class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value

class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass

class InterpreterVisitor(gramatica_v4Visitor):

    def __init__(self):
        self.tabla = TablaSimbolos()

    # ROOT
    def visitRoot(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # BLOCK
    def visitBlock(self, ctx):
        self.tabla.push_scope()
        for stmt in ctx.statement():
            self.visit(stmt)
        self.tabla.pop_scope()

    # DECLARACIÓN
    def visitDeclaration(self, ctx):
        self.visit(ctx.declarationStatement())

    def visitDeclarationStatement(self, ctx):
        nombre = ctx.VAR().getText()
        tipo = ctx.tipo().getText()
        decl = ctx.DECL().getText()  # var / let / const

        valor = None

        if ctx.arrayLiteral():
            valor = self.visit(ctx.arrayLiteral())
        elif ctx.valueExpr():
            valor = self.visit(ctx.valueExpr())

        self.tabla.declarar(
            nombre,
            tipo,
            valor,
            mutable=(decl != "const")
        )

    # ARRAY
    def visitArrayLiteral(self, ctx):
        return [self.visit(e) for e in ctx.expr()]

    # ASIGNACIÓN
    def visitAssignment(self, ctx):
        self.visit(ctx.assignmentStatement())

    def visitAssignmentStatement(self, ctx):
        nombre = ctx.VAR().getText()
        valor = self.visit(ctx.expr())

        var = self.tabla.obtener(nombre)

        if not var.get("mutable", True):
            raise Exception(f"Error: '{nombre}' es const y no puede modificarse")

        self.tabla.asignar(nombre, valor)

    # FUNCIONES
    def visitFunctionDecl(self, ctx):
        nombre = ctx.VAR().getText()
        tipo = ctx.tipo().getText()

        parametros = []
        if ctx.paramList():
            for p in ctx.paramList().param():
                parametros.append((p.VAR().getText(), p.tipo().getText()))

        self.tabla.declarar_funcion(nombre, tipo, parametros, ctx)

    def visitFunctionCall(self, ctx):
        func = self.tabla.obtener_funcion(ctx.VAR().getText())

        args = []
        if ctx.argList():
            args = [self.visit(e) for e in ctx.argList().expr()]

        self.tabla.push_scope()

        for i, (n, t) in enumerate(func["parametros"]):
            self.tabla.declarar(n, t, args[i])

        try:
            self.visit(func["ctx"].block())
        except ReturnValue as r:
            self.tabla.pop_scope()
            return r.value

        self.tabla.pop_scope()
        return None

    def visitReturnStmt(self, ctx):
        val = self.visit(ctx.expr()) if ctx.expr() else None
        raise ReturnValue(val)

    # CONTROL DE FLUJO
    def visitIfStatement(self, ctx):
        if self.visit(ctx.condition()):
            self.visit(ctx.block(0))
        elif ctx.ELSE():
            self.visit(ctx.block(1))

    def visitWhileStatement(self, ctx):
        while self.visit(ctx.condition()):
            try:
                self.visit(ctx.block())
            except ContinueException:
                continue
            except BreakException:
                break

    def visitForStatement(self, ctx):
        self.tabla.push_scope()

        if ctx.forInit():
            if ctx.forInit().declarationStatement():
                self.visit(ctx.forInit().declarationStatement())
            else:
                self.visit(ctx.forInit().assignmentStatement())

        while True:
            if ctx.condition():
                if not self.visit(ctx.condition()):
                    break

            try:
                for stmt in ctx.block().statement():
                    self.visit(stmt)
            except ContinueException:
                pass
            except BreakException:
                break

            if ctx.forUpdate():
                self.visit(ctx.forUpdate().assignmentStatement())

        self.tabla.pop_scope()

    def visitBreakStmt(self, ctx):
        raise BreakException()

    def visitContinueStmt(self, ctx):
        raise ContinueException()

    # SWITCH
    def visitSwitchStatement(self, ctx):

        valor_switch = self.visit(ctx.expr())

        ejecutado = False

        for case_ctx in ctx.caseClause():

            valor_case = self.visit(case_ctx.literal())

            if valor_switch == valor_case:

                ejecutado = True

                try:

                    for stmt in case_ctx.statement():
                        self.visit(stmt)

                except BreakException:
                    return

                break

        if not ejecutado and ctx.defaultClause():

            try:

                for stmt in ctx.defaultClause().statement():
                    self.visit(stmt)

            except BreakException:
                return
            
    def visitLiteral(self, ctx):

        if ctx.NUM():
            return int(ctx.NUM().getText())

        if ctx.FLOAT():
            return float(ctx.FLOAT().getText())

        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]

    # IMPORT (no-op)
    def visitImportStmt(self, ctx):
        # No hace nada por ahora
        return

    # CONDICIONES
    def visitCondition(self, ctx):

        if ctx.AND():
            return self.visit(ctx.condition(0)) and self.visit(ctx.condition(1))

        if ctx.OR():
            return self.visit(ctx.condition(0)) or self.visit(ctx.condition(1))

        if ctx.NOT():
            return not self.visit(ctx.condition(0))

        if ctx.relop():
            a = self.visit(ctx.expr(0))
            b = self.visit(ctx.expr(1))
            op = ctx.relop().getText()

            return {
                '>': a > b,
                '<': a < b,
                '>=': a >= b,
                '<=': a <= b,
                '==': a == b,
                '!=': a != b
            }[op]

        if ctx.TRUE():
            return True

        if ctx.FALSE():
            return False

        if ctx.condition():
            return self.visit(ctx.condition(0))

    # EXPRESIONES
    def visitExpr(self, ctx):

        # LITERALES
        if ctx.NUM():
            return int(ctx.NUM().getText())

        if ctx.FLOAT():
            return float(ctx.FLOAT().getText())

        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]

        if ctx.TRUE():
            return True

        if ctx.FALSE():
            return False

        # ARRAY ACCESS
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '[':
            nombre = ctx.VAR().getText()
            arr = self.tabla.obtener(nombre)["valor"]
            index = self.visit(ctx.expr(0))

            if not isinstance(arr, list):
                raise Exception("Error: variable no es un array")

            return arr[index]

        # VARIABLE
        if ctx.VAR():
            return self.tabla.obtener(ctx.VAR().getText())["valor"]

        # FUNCTION CALL
        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        # OPERACIONES
        if len(ctx.expr()) == 2:
            a = self.visit(ctx.expr(0))
            b = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()

            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return a // b
            if op == '%': return a % b

        # PARENTESIS
        if ctx.expr():
            return self.visit(ctx.expr(0))

    # PRINT
    def visitPrintStmt(self, ctx):
        valor = self.visit(ctx.expr())
        print(valor)