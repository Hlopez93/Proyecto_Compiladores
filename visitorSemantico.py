from ExpresionesVisitor import ExpresionesVisitor
from ExpresionesParser import ExpresionesParser
from tablaSimbolos import TablaSimbolos

class SemanticVisitor(ExpresionesVisitor):

    def __init__(self):
        self.tabla = TablaSimbolos()

    # ---------------- PROGRAMA ----------------
    def visitRoot(self, ctx: ExpresionesParser.RootContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    # ---------------- DECLARACION ----------------
    def visitDeclaration(self, ctx: ExpresionesParser.DeclarationContext):
        nombre = ctx.VAR().getText()
        tipo = ctx.tipo().getText()

        # Validar si ya existe en el scope actual
        scope_actual = self.tabla.scopes[-1]
        if nombre in scope_actual:
            raise Exception(f"Error: Variable '{nombre}' ya declarada en este ámbito")

        # Evaluar expresión si existe
        valor = None
        if ctx.expr():
            valor = self.visit(ctx.expr())

        # Guardar en tabla
        self.tabla.declarar(nombre, tipo, valor)

    # ---------------- ASIGNACION ----------------
    def visitAssignment(self, ctx: ExpresionesParser.AssignmentContext):
        nombre = ctx.VAR().getText()

        # Verificar que exista
        simbolo = self.tabla.obtener(nombre)

        # Evaluar valor
        valor = self.visit(ctx.expr())

        # Asignar
        self.tabla.asignar(nombre, valor)

    # ---------------- BLOQUES ----------------
    def visitBlock(self, ctx: ExpresionesParser.BlockContext):
        self.tabla.push_scope()

        for stmt in ctx.statement():
            self.visit(stmt)

        self.tabla.pop_scope()

    # ---------------- IF ----------------
    def visitIfStatement(self, ctx: ExpresionesParser.IfStatementContext):
        self.visit(ctx.condition())
        self.visit(ctx.block(0))

        if ctx.ELSE():
            self.visit(ctx.block(1))

    # ---------------- WHILE ----------------
    def visitWhileStatement(self, ctx: ExpresionesParser.WhileStatementContext):
        self.visit(ctx.condition())
        self.visit(ctx.block())

    # ---------------- FOR ----------------
    def visitForStatement(self, ctx: ExpresionesParser.ForStatementContext):

        self.tabla.push_scope()

        if ctx.declaration():
            self.visit(ctx.declaration())
        elif ctx.assignment():
            self.visit(ctx.assignment())

        if ctx.condition():
            self.visit(ctx.condition())

        if ctx.assignment():
            self.visit(ctx.assignment())

        self.visit(ctx.block())

        self.tabla.pop_scope()

    # ---------------- PRINT ----------------
    def visitPrintStmt(self, ctx: ExpresionesParser.PrintStmtContext):
        self.visit(ctx.expr())

    # ---------------- CONDICIONES ----------------
    def visitCondition(self, ctx: ExpresionesParser.ConditionContext):

        if ctx.AND():
            self.visit(ctx.condition(0))
            self.visit(ctx.condition(1))

        elif ctx.OR():
            self.visit(ctx.condition(0))
            self.visit(ctx.condition(1))

        elif ctx.NOT():
            self.visit(ctx.condition(0))

        elif ctx.relop():
            self.visit(ctx.expr(0))
            self.visit(ctx.expr(1))

        elif ctx.condition():
            self.visit(ctx.condition(0))

    # ---------------- EXPRESIONES ----------------
    def visitExpr(self, ctx: ExpresionesParser.ExprContext):

        # Paréntesis
        if ctx.expr() and ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expr(0))

        # Operaciones binarias
        if len(ctx.expr()) == 2:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left  # (solo validación, no cálculo real aquí)

        # Literales
        if ctx.NUM():
            return int(ctx.NUM().getText())

        if ctx.FLOAT():
            return float(ctx.FLOAT().getText())

        if ctx.STRING():
            return ctx.STRING().getText()

        if ctx.TRUE():
            return True

        if ctx.FALSE():
            return False

        # Variable
        if ctx.VAR():
            simbolo = self.tabla.obtener(ctx.VAR().getText())
            return simbolo["valor"]

        # Función (placeholder)
        if ctx.functionCall():
            return None