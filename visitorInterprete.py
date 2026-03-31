from ExpresionesVisitor import ExpresionesVisitor
from ExpresionesParser import ExpresionesParser
from tablaSimbolos import TablaSimbolos

class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value

class InterpreterVisitor(ExpresionesVisitor):

    def __init__(self):
        self.tabla = TablaSimbolos()

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

        valor = None
        if ctx.expr():
            valor = self.visit(ctx.expr())

        self.tabla.declarar(nombre, tipo, valor)

    def visitAssignment(self, ctx):
        self.tabla.asignar(ctx.VAR().getText(), self.visit(ctx.expr()))

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

    def visitIfStatement(self, ctx):
        if self.visit(ctx.condition()):
            self.visit(ctx.block(0))
        elif ctx.ELSE():
            self.visit(ctx.block(1))

    def visitWhileStatement(self, ctx):
        while self.visit(ctx.condition()):
            self.visit(ctx.block())

    def visitForStatement(self, ctx):
        if ctx.declaration(): self.visit(ctx.declaration())
        elif ctx.assignment(): self.visit(ctx.assignment())

        while True:
            if ctx.condition() and not self.visit(ctx.condition()):
                break

            self.visit(ctx.block())

            if ctx.assignment(): self.visit(ctx.assignment())

    def visitCondition(self, ctx):
        if ctx.AND(): return self.visit(ctx.condition(0)) and self.visit(ctx.condition(1))
        if ctx.OR(): return self.visit(ctx.condition(0)) or self.visit(ctx.condition(1))
        if ctx.NOT(): return not self.visit(ctx.condition(0))

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

        if ctx.TRUE(): return True
        if ctx.FALSE(): return False

        if ctx.condition(): return self.visit(ctx.condition(0))

    def visitExpr(self, ctx):
        if ctx.NUM(): return int(ctx.NUM().getText())
        if ctx.FLOAT(): return float(ctx.FLOAT().getText())
        if ctx.STRING(): return ctx.STRING().getText()[1:-1]
        if ctx.TRUE(): return True
        if ctx.FALSE(): return False

        if ctx.VAR():
            return self.tabla.obtener(ctx.VAR().getText())["valor"]

        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        if len(ctx.expr()) == 2:
            a = self.visit(ctx.expr(0))
            b = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()

            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return a // b

        if ctx.expr():
            return self.visit(ctx.expr(0))
