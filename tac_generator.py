from gramatica_v3Visitor import gramatica_v3Visitor

class TACGenerator(gramatica_v3Visitor):

    def __init__(self):
        self.code = []
        self.temp_count = 0
        self.label_count = 0

        self.break_stack = []
        self.continue_stack = []

    # ========================
    # UTILIDADES
    # ========================
    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def emit(self, instr):
        self.code.append(instr)

    def get_code(self):
        return "\n".join(self.code)

    # ========================
    # ROOT
    # ========================
    def visitRoot(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # ========================
    # DECLARACIÓN
    # ========================
    def visitDeclaration(self, ctx):
        self.visit(ctx.declarationStatement())

    def visitDeclarationStatement(self, ctx):
        nombre = ctx.VAR().getText()

        if ctx.arrayLiteral():
            valores = [self.visit(e) for e in ctx.arrayLiteral().expr()]
            self.emit(f"{nombre} = [{', '.join(map(str, valores))}]")

        elif ctx.expr():
            val = self.visit(ctx.expr())
            self.emit(f"{nombre} = {val}")

    # ========================
    # ASIGNACIÓN
    # ========================
    def visitAssignmentStatement(self, ctx):
        nombre = ctx.VAR().getText()
        val = self.visit(ctx.expr())
        self.emit(f"{nombre} = {val}")

    # ========================
    # EXPRESIONES
    # ========================
    def visitExpr(self, ctx):
        if ctx.NUM():
            return ctx.NUM().getText()

        if ctx.FLOAT():
            return ctx.FLOAT().getText()

        if ctx.STRING():
            return ctx.STRING().getText()

        if ctx.VAR():
            return ctx.VAR().getText()

        # acceso array: a[i]
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '[':
            nombre = ctx.getChild(0).getText()
            index = self.visit(ctx.expr(0))

            temp = self.new_temp()
            self.emit(f"{temp} = {nombre}[{index}]")
            return temp

        # binaria
        if len(ctx.expr()) == 2:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()

            temp = self.new_temp()
            self.emit(f"{temp} = {left} {op} {right}")
            return temp

        if ctx.expr():
            return self.visit(ctx.expr(0))

    # ========================
    # CONDICIÓN
    # ========================
    def visitCondition(self, ctx):
        if ctx.relop():
            a = self.visit(ctx.expr(0))
            b = self.visit(ctx.expr(1))
            op = ctx.relop().getText()
            return f"{a} {op} {b}"

        if ctx.AND():
            a = self.visit(ctx.condition(0))
            b = self.visit(ctx.condition(1))
            temp = self.new_temp()
            self.emit(f"{temp} = {a} && {b}")
            return temp

        if ctx.OR():
            a = self.visit(ctx.condition(0))
            b = self.visit(ctx.condition(1))
            temp = self.new_temp()
            self.emit(f"{temp} = {a} || {b}")
            return temp

        if ctx.NOT():
            val = self.visit(ctx.condition(0))
            temp = self.new_temp()
            self.emit(f"{temp} = !{val}")
            return temp

        if ctx.TRUE():
            return "true"

        if ctx.FALSE():
            return "false"

        if ctx.condition():
            return self.visit(ctx.condition(0))

    # ========================
    # IF
    # ========================
    def visitIfStatement(self, ctx):
        cond = self.visit(ctx.condition())

        Ltrue = self.new_label()
        Lend = self.new_label()

        self.emit(f"if {cond} goto {Ltrue}")

        if ctx.ELSE():
            self.visit(ctx.block(1))

        self.emit(f"goto {Lend}")
        self.emit(f"{Ltrue}:")

        self.visit(ctx.block(0))

        self.emit(f"{Lend}:")

    # ========================
    # WHILE
    # ========================
    def visitWhileStatement(self, ctx):
        Lstart = self.new_label()
        Lend = self.new_label()

        self.break_stack.append(Lend)
        self.continue_stack.append(Lstart)

        self.emit(f"{Lstart}:")

        cond = self.visit(ctx.condition())
        self.emit(f"if not {cond} goto {Lend}")

        self.visit(ctx.block())
        self.emit(f"goto {Lstart}")

        self.emit(f"{Lend}:")

        self.break_stack.pop()
        self.continue_stack.pop()

    # ========================
    # FOR
    # ========================
    def visitForStatement(self, ctx):
        if ctx.forInit():
            self.visit(ctx.forInit())

        Lstart = self.new_label()
        Lupdate = self.new_label()
        Lend = self.new_label()

        self.break_stack.append(Lend)
        self.continue_stack.append(Lupdate)

        self.emit(f"{Lstart}:")

        if ctx.condition():
            cond = self.visit(ctx.condition())
            self.emit(f"if not {cond} goto {Lend}")

        self.visit(ctx.block())

        self.emit(f"{Lupdate}:")

        if ctx.forUpdate():
            self.visit(ctx.forUpdate())

        self.emit(f"goto {Lstart}")
        self.emit(f"{Lend}:")

        self.break_stack.pop()
        self.continue_stack.pop()

    # ========================
    # BREAK / CONTINUE
    # ========================
    def visitBreakStmt(self, ctx):
        self.emit(f"goto {self.break_stack[-1]}")

    def visitContinueStmt(self, ctx):
        self.emit(f"goto {self.continue_stack[-1]}")

    # ========================
    # PRINT
    # ========================
    def visitPrintStmt(self, ctx):
        val = self.visit(ctx.expr())
        self.emit(f"print {val}")

    # ========================
    # RETURN
    # ========================
    def visitReturnStmt(self, ctx):
        if ctx.expr():
            val = self.visit(ctx.expr())
            self.emit(f"return {val}")
        else:
            self.emit("return")

    # ========================
    # FUNCIONES
    # ========================
    def visitFunctionDecl(self, ctx):
        nombre = ctx.VAR().getText()

        self.emit(f"begin_func {nombre}")

        if ctx.paramList():
            for p in ctx.paramList().param():
                self.emit(f"param {p.VAR().getText()}")

        self.visit(ctx.block())

        self.emit(f"end_func {nombre}")

    # ========================
    # LLAMADAS A FUNCIÓN
    # ========================
    def visitFunctionCall(self, ctx):
        nombre = ctx.VAR().getText()

        args = []
        if ctx.argList():
            args = [self.visit(e) for e in ctx.argList().expr()]

        for arg in args:
            self.emit(f"param {arg}")

        temp = self.new_temp()
        self.emit(f"{temp} = call {nombre}, {len(args)}")

        return temp