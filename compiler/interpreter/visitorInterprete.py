from compiler.gramatica_v3Visitor import gramatica_v3Visitor
from compiler.semantic.tablaSimbolos import TablaSimbolos


class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value


class BreakException(Exception):
    pass


class ContinueException(Exception):
    pass


class InterpreterVisitor(gramatica_v3Visitor):

    def __init__(self):
        self.tabla = TablaSimbolos()

    # ================= ROOT =================
    def visitRoot(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # ================= BLOCK =================
    def visitBlock(self, ctx):
        self.tabla.push_scope()
        try:
            for stmt in ctx.statement():
                self.visit(stmt)
        finally:
            # SIEMPRE liberar el scope, incluso si ReturnValue/BreakException propagan
            self.tabla.pop_scope()

    # ================= DECLARACION =================
    def visitDeclaration(self, ctx):
        self.visit(ctx.declarationStatement())

    def visitDeclarationStatement(self, ctx):
        nombre = ctx.VAR().getText()
        tipo = ctx.tipo().getText()
        decl = ctx.DECL().getText()

        valor = None
        if ctx.arrayLiteral():
            valor = self.visit(ctx.arrayLiteral())
        elif ctx.expr():
            valor = self.visit(ctx.expr())

        self.tabla.declarar(nombre, tipo, valor, mutable=(decl != "const"))

    def visitArrayLiteral(self, ctx):
        return [self.visit(e) for e in ctx.expr()]

    # ================= ASIGNACION =================
    def visitAssignment(self, ctx):
        self.visit(ctx.assignmentStatement())

    def visitAssignmentStatement(self, ctx):
        nombre = ctx.VAR().getText()
        valor = self.visit(ctx.expr())

        var = self.tabla.obtener(nombre)

        if not var.get("mutable", True):
            raise Exception(f"Error: '{nombre}' es const")

        self.tabla.asignar(nombre, valor)

    # ================= FUNCIONES =================
    def visitFunctionDecl(self, ctx):
        nombre = ctx.VAR().getText()
        tipo = ctx.tipo().getText()

        params = []
        if ctx.paramList():
            for p in ctx.paramList().param():
                params.append((p.VAR().getText(), p.tipo().getText()))

        self.tabla.declarar_funcion(nombre, tipo, params, ctx)

    def visitFunctionCall(self, ctx):
        func = self.tabla.obtener_funcion(ctx.VAR().getText())

        args = []
        if ctx.argList():
            args = [self.visit(e) for e in ctx.argList().expr()]

        self.tabla.push_scope()
        result = None

        try:
            for i, (n, t) in enumerate(func["parametros"]):
                self.tabla.declarar(n, t, args[i])

            try:
                for stmt in func["ctx"].block().statement():
                    self.visit(stmt)
            except ReturnValue as r:
                result = r.value
        finally:
            self.tabla.pop_scope()

        return result

    def visitReturnStmt(self, ctx):
        val = self.visit(ctx.expr()) if ctx.expr() else None
        raise ReturnValue(val)

    # ================= CONTROL =================
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

        try:
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
                    self.visit(ctx.block())
                except ContinueException:
                    pass
                except BreakException:
                    break

                if ctx.forUpdate():
                    self.visit(ctx.forUpdate().assignmentStatement())
        finally:
            self.tabla.pop_scope()

    def visitBreakStmt(self, ctx):
        raise BreakException()

    def visitContinueStmt(self, ctx):
        raise ContinueException()

    # ================= CONDICIONES =================
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

        # PAI condition PAD
        if ctx.condition():
            return self.visit(ctx.condition(0))

    # ================= EXPRESIONES =================
    def visitExpr(self, ctx):
        # expr SUM term  |  expr RES term
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr())
            right = self.visit(ctx.term())
            op = ctx.getChild(1).getText()
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            else:
                raise Exception(f"Operador desconocido en expr: {op}")
        # just a term
        return self.visit(ctx.term())

    def visitTerm(self, ctx):
        # term MUL factor  |  term DIV factor  |  term MOD factor
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.term())
            right = self.visit(ctx.factor())
            op = ctx.getChild(1).getText()
            if op == '*':
                return left * right
            elif op == '/':
                if isinstance(left, int) and isinstance(right, int):
                    return left // right
                return left / right
            elif op == '%':
                return left % right
            else:
                raise Exception(f"Operador desconocido en term: {op}")
        # just a factor
        return self.visit(ctx.factor())

    def visitFactor(self, ctx):
        # NUM
        if ctx.NUM():
            return int(ctx.NUM().getText())

        # FLOAT
        if ctx.FLOAT():
            return float(ctx.FLOAT().getText())

        # STRING
        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]

        # TRUE / FALSE
        if ctx.TRUE():
            return True
        if ctx.FALSE():
            return False

        # Array access: VAR '[' expr ']'  (4 children) - check BEFORE plain VAR
        if ctx.getChildCount() == 4:
            nombre = ctx.VAR().getText()
            arr = self.tabla.obtener(nombre)["valor"]
            index = self.visit(ctx.expr())
            return arr[index]

        # Function call - check BEFORE plain VAR
        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        # Plain variable
        if ctx.VAR():
            return self.tabla.obtener(ctx.VAR().getText())["valor"]

        # Parenthesized expression: '(' expr ')'
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())

        raise Exception(f"Factor no soportado: {ctx.getText()}")

    # ================= PRINT =================
    def visitPrintStmt(self, ctx):
        print(self.visit(ctx.expr()))