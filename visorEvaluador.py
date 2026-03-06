from ExpresionesVisitor import ExpresionesVisitor

class visorEvaluador(ExpresionesVisitor):

    def __init__(self):
        self.memory = {}  # tabla de símbolos

    # root
    def visitRoot(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # declaración
    def visitDeclaration(self, ctx):
        var_name = ctx.ID().getText()

        if ctx.expression():
            value = self.visit(ctx.expression())
            self.memory[var_name] = value
        else:
            self.memory[var_name] = 0

    # asignación
    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.memory[var_name] = value

    # IF
    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.expression())

        if condition:
            self.visit(ctx.block(0))
        elif ctx.block(1):
            self.visit(ctx.block(1))

    # bloque
    def visitBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # EXPRESIONES
    def visitAdditiveExpression(self, ctx):
        result = self.visit(ctx.multiplicativeExpression(0))

        for i in range(1, len(ctx.multiplicativeExpression())):
            right = self.visit(ctx.multiplicativeExpression(i))
            op = ctx.getChild(2*i - 1).getText()

            if op == '+':
                result += right
            else:
                result -= right

        return result

    def visitMultiplicativeExpression(self, ctx):
        result = self.visit(ctx.unaryExpression(0))

        for i in range(1, len(ctx.unaryExpression())):
            right = self.visit(ctx.unaryExpression(i))
            op = ctx.getChild(2*i - 1).getText()

            if op == '*':
                result *= right
            else:
                result /= right

        return result

    def visitPrimary(self, ctx):
        if ctx.NUM():
            return int(ctx.NUM().getText())
        elif ctx.ID():
            var_name = ctx.ID().getText()
            return self.memory.get(var_name, 0)
        else:
            return self.visit(ctx.expression())