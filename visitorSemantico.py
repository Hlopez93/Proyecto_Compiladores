from ExpresionesVisitor import ExpresionesVisitor
from ExpresionesParser import ExpresionesParser
from tablaSimbolos import TablaSimbolos

class SemanticVisitor(ExpresionesVisitor):

    def __init__(self):
        self.tabla = TablaSimbolos()
        self.current_function = None

    def visitRoot(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitBlock(self, ctx):
        self.tabla.push_scope()
        for stmt in ctx.statement():
            self.visit(stmt)
        self.tabla.pop_scope()

    def visitDeclaration(self, ctx):
        nombre = ctx.VAR().getText()
        tipo = ctx.tipo().getText()

        if ctx.expr():
            tipo_expr = self.visit(ctx.expr())
            if tipo_expr != tipo:
                raise Exception("Error semántico: tipos incompatibles en declaración")

        self.tabla.declarar(nombre, tipo)

    def visitAssignment(self, ctx):
        nombre = ctx.VAR().getText()
        var = self.tabla.obtener(nombre)

        tipo_expr = self.visit(ctx.expr())

        if var["tipo"] != tipo_expr:
            raise Exception("Error semántico: tipos incompatibles en asignación")

    def visitFunctionDecl(self, ctx):
        nombre = ctx.VAR().getText()
        tipo_retorno = ctx.tipo().getText()

        parametros = []
        if ctx.paramList():
            for p in ctx.paramList().param():
                parametros.append((p.VAR().getText(), p.tipo().getText()))

        self.tabla.declarar_funcion(nombre, tipo_retorno, parametros, ctx)

        prev = self.current_function
        self.current_function = tipo_retorno

        self.tabla.push_scope()
        for n, t in parametros:
            self.tabla.declarar(n, t)

        self.visit(ctx.block())

        self.tabla.pop_scope()
        self.current_function = prev

    def visitReturnStmt(self, ctx):
        if self.current_function is None:
            raise Exception("Error semántico: return fuera de función")

        if ctx.expr():
            tipo_expr = self.visit(ctx.expr())
            if tipo_expr != self.current_function:
                raise Exception("Error semántico: tipo de retorno incorrecto")
        else:
            if self.current_function != "void":
                raise Exception("Error semántico: return vacío en función no void")

    def visitFunctionCall(self, ctx):
        nombre = ctx.VAR().getText()
        func = self.tabla.obtener_funcion(nombre)

        args = []
        if ctx.argList():
            args = [self.visit(e) for e in ctx.argList().expr()]

        if len(args) != len(func["parametros"]):
            raise Exception("Error: número incorrecto de argumentos")

        for i, (n, t) in enumerate(func["parametros"]):
            if args[i] != t:
                raise Exception("Error: tipo de argumento incorrecto")

        return func["retorno"]

    def visitIfStatement(self, ctx):
        if self.visit(ctx.condition()) != "bool":
            raise Exception("Error: condición de if debe ser bool")

        self.visit(ctx.block(0))
        if ctx.ELSE():
            self.visit(ctx.block(1))

    def visitWhileStatement(self, ctx):
        if self.visit(ctx.condition()) != "bool":
            raise Exception("Error: condición de while debe ser bool")

        self.visit(ctx.block())

    def visitForStatement(self, ctx):
        if ctx.condition() and self.visit(ctx.condition()) != "bool":
            raise Exception("Error: condición de for debe ser bool")
        self.visit(ctx.block())

    def visitCondition(self, ctx):
        if ctx.AND() or ctx.OR():
            if self.visit(ctx.condition(0)) != "bool" or self.visit(ctx.condition(1)) != "bool":
                raise Exception("Error: operadores lógicos requieren booleanos")
            return "bool"

        if ctx.NOT():
            if self.visit(ctx.condition(0)) != "bool":
                raise Exception("Error: NOT requiere booleano")
            return "bool"

        if ctx.relop():
            if self.visit(ctx.expr(0)) != self.visit(ctx.expr(1)):
                raise Exception("Error: comparación inválida")
            return "bool"

        if ctx.TRUE() or ctx.FALSE():
            return "bool"

        if ctx.condition():
            return self.visit(ctx.condition(0))

    def visitExpr(self, ctx):
        if ctx.NUM(): return "int"
        if ctx.FLOAT(): return "float"
        if ctx.STRING(): return "string"
        if ctx.TRUE() or ctx.FALSE(): return "bool"

        if ctx.VAR():
            return self.tabla.obtener(ctx.VAR().getText())["tipo"]

        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        if len(ctx.expr()) == 2:
            t1 = self.visit(ctx.expr(0))
            t2 = self.visit(ctx.expr(1))

            if t1 != t2:
                raise Exception("Error: operación entre tipos incompatibles")

            return t1

        if ctx.expr():
            return self.visit(ctx.expr(0))