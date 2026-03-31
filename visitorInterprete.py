from ExpresionesVisitor import ExpresionesVisitor
from ExpresionesParser import ExpresionesParser

class InterpreterVisitor(ExpresionesVisitor):

    def __init__(self, tabla):
        self.tabla = tabla  # tabla de símbolos (scopes)
    
    # ---------------- PROGRAMA ----------------
    def visitRoot(self, ctx: ExpresionesParser.RootContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    # ---------------- DECLARACION ----------------
    def visitDeclaration(self, ctx: ExpresionesParser.DeclarationContext):
        nombre = ctx.VAR().getText()

        valor = None
        if ctx.expr():
            valor = self.visit(ctx.expr())

        # Asignamos valor en tabla (ya declarada en semántico)
        self.tabla.asignar(nombre, valor)

    # ---------------- ASIGNACION ----------------
    def visitAssignment(self, ctx: ExpresionesParser.AssignmentContext):
        nombre = ctx.VAR().getText()
        valor = self.visit(ctx.expr())

        self.tabla.asignar(nombre, valor)

    # ---------------- PRINT ----------------
    def visitPrintStmt(self, ctx: ExpresionesParser.PrintStmtContext):
        valor = self.visit(ctx.expr())
        print(valor)

    # ---------------- BLOQUES ----------------
    def visitBlock(self, ctx: ExpresionesParser.BlockContext):
        self.tabla.push_scope()

        for stmt in ctx.statement():
            self.visit(stmt)

        self.tabla.pop_scope()

    # ---------------- IF ----------------
    def visitIfStatement(self, ctx: ExpresionesParser.IfStatementContext):
        condicion = self.visit(ctx.condition())

        if condicion:
            self.visit(ctx.block(0))
        elif ctx.ELSE():
            self.visit(ctx.block(1))

    # ---------------- WHILE ----------------
    def visitWhileStatement(self, ctx: ExpresionesParser.WhileStatementContext):
        while self.visit(ctx.condition()):
            self.visit(ctx.block())

    # ---------------- FOR ----------------
    def visitForStatement(self, ctx: ExpresionesParser.ForStatementContext):

        self.tabla.push_scope()

        # Inicialización
        if ctx.declaration():
            self.visit(ctx.declaration())
        elif ctx.assignment():
            self.visit(ctx.assignment())

        # Condición
        while True:
            if ctx.condition():
                if not self.visit(ctx.condition()):
                    break

            # Cuerpo
            self.visit(ctx.block())

            # Actualización
            if ctx.assignment():
                self.visit(ctx.assignment())

        self.tabla.pop_scope()

    # ---------------- CONDICIONES ----------------
    def visitCondition(self, ctx: ExpresionesParser.ConditionContext):

        if ctx.AND():
            return self.visit(ctx.condition(0)) and self.visit(ctx.condition(1))

        if ctx.OR():
            return self.visit(ctx.condition(0)) or self.visit(ctx.condition(1))

        if ctx.NOT():
            return not self.visit(ctx.condition(0))

        if ctx.relop():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.relop().getText()

            if op == '>': return left > right
            if op == '<': return left < right
            if op == '>=': return left >= right
            if op == '<=': return left <= right
            if op == '==': return left == right
            if op == '!=': return left != right

        if ctx.TRUE():
            return True

        if ctx.FALSE():
            return False

        if ctx.condition():
            return self.visit(ctx.condition(0))

    # ---------------- EXPRESIONES ----------------
    def visitExpr(self, ctx: ExpresionesParser.ExprContext):

        # Paréntesis
        if ctx.expr() and ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expr(0))

        # Operaciones binarias
        if len(ctx.expr()) == 2:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()

            if op == '+': return left + right
            if op == '-': return left - right
            if op == '*': return left * right
            if op == '/': return left / right

        # Número entero
        if ctx.NUM():
            return int(ctx.NUM().getText())

        # Float
        if ctx.FLOAT():
            return float(ctx.FLOAT().getText())

        # String
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')

        # Booleanos
        if ctx.TRUE():
            return True
        if ctx.FALSE():
            return False

        # Variable
        if ctx.VAR():
            return self.tabla.obtener(ctx.VAR().getText())["valor"]

        # Llamada a función (placeholder por ahora)
        if ctx.functionCall():
            return self.visit(ctx.functionCall())

    # ---------------- FUNCION CALL ----------------
    def visitFunctionCall(self, ctx: ExpresionesParser.FunctionCallContext):
        nombre = ctx.VAR().getText()
        print(f"Llamada a función '{nombre}' aún no implementada")
        return None