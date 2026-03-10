from ExpresionesVisitor import ExpresionesVisitor

class visorEvaluador(ExpresionesVisitor):

    def __init__(self):
        self.memory = {}

    # programa
    def visitRoot(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # declaracion
    def visitDeclaration(self, ctx):
        var = ctx.VAR().getText()
        self.memory[var] = 0

    # condicion
    def visitCondition(self, ctx):
        # NOT
        if ctx.NOT():
            return not self.visit(ctx.condition(0))

        # AND
        if ctx.AND():
            left = self.visit(ctx.condition(0))
            right = self.visit(ctx.condition(1))
            return left and right

        # OR
        if ctx.OR():
            left = self.visit(ctx.condition(0))
            right = self.visit(ctx.condition(1))
            return left or right

        # Comparación relacional
        if ctx.relop():

            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.relop().getText()

            if op == ">":
                return left > right
            if op == "<":
                return left < right
            if op == ">=":
                return left >= right
            if op == "<=":
                return left <= right
            if op == "==":
                return left == right
            if op == "!=":
                return left != right

        # paréntesis
        if ctx.condition():
            return self.visit(ctx.condition(0))

    # asignacion
    def visitAssignment(self, ctx):
        var = ctx.VAR().getText()
        value = self.visit(ctx.expr())
        self.memory[var] = value

    # if
    def visitIfStatement(self, ctx):
        cond = self.visit(ctx.condition())

        if cond:
            self.visit(ctx.block(0))
        elif ctx.block(1):
            self.visit(ctx.block(1))

    # bloque
    def visitBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # expresiones
    def visitExpr(self, ctx):
        if ctx.NUM():
            return int(ctx.NUM().getText())

        if ctx.VAR():
            return self.memory.get(ctx.VAR().getText(), 0)

        if ctx.getChildCount() == 3:

            if ctx.getChild(0).getText() == "(":
                return self.visit(ctx.expr(0))

            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()

            if op == "+":
                return left + right
            if op == "-":
                return left - right
            if op == "*":
                return left * right
            if op == "/":
                return left / right