from flask import ctx

from compiler.gramatica_v4Visitor import gramatica_v4Visitor


class TACGenerator(gramatica_v4Visitor):

    def __init__(self):
        self.code = []
        self.temp_count = 0
        self.label_count = 0
        self.break_stack = []
        self.continue_stack = []

    # ================= UTIL =================
    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def emit(self, instr):
        self.code.append(instr)

    # ================= ROOT =================
    def visitRoot(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # ================= WRAPPERS =================
    def visitDeclaration(self, ctx):
        self.visit(ctx.declarationStatement())

    def visitAssignment(self, ctx):
        self.visit(ctx.assignmentStatement())

    # ================= DECLARACION =================
    def visitDeclarationStatement(self, ctx):
        nombre = ctx.VAR().getText()

        if ctx.arrayLiteral():
            valores = [self.visit(e) for e in ctx.arrayLiteral().expr()]
            self.emit(f"{nombre} = [{', '.join(map(str, valores))}]")

        elif ctx.valueExpr():
            val = self.visit(ctx.valueExpr())
            self.emit(f"{nombre} = {val}")

    # ================= ASIGNACION =================
    def visitAssignmentStatement(self, ctx):
        nombre = ctx.VAR().getText()
        val = self.visit(ctx.valueExpr())
        self.emit(f"{nombre} = {val}")

    # ================= EXPRESIONES =================
    def visitExpr(self, ctx):

        # expr: expr + term | expr - term
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() in ['+', '-']:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()

            temp = self.new_temp()
            self.emit(f"{temp} = {left} {op} {right}")
            return temp

        return self.visit(ctx.term())

    def visitTerm(self, ctx):

        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()

            temp = self.new_temp()
            self.emit(f"{temp} = {left} {op} {right}")
            return temp

        return self.visit(ctx.factor())

    def visitFactor(self, ctx):

        # NUM
        if ctx.NUM():
            return ctx.NUM().getText()

        # FLOAT
        if ctx.FLOAT():
            return ctx.FLOAT().getText()

        # STRING
        if ctx.STRING():
            return ctx.STRING().getText()

        # BOOL
        if ctx.TRUE():
            return "1"

        if ctx.FALSE():
            return "0"

        # array[index]: VAR '[' expr ']' — check BEFORE plain VAR
        if ctx.getChildCount() == 4:
            nombre = ctx.VAR().getText()
            index = self.visit(ctx.expr())

            temp = self.new_temp()
            self.emit(f"{temp} = {nombre}[{index}]")
            return temp

        # FUNCTION CALL — check BEFORE plain VAR
        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        # VARIABLE
        if ctx.VAR():
            return ctx.VAR().getText()

        # (expr)
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())

        return "0"

    # ================= CONDICIONES =================
    def visitCondition(self, ctx):

        if ctx.relop():
            a = self.visit(ctx.expr(0))
            b = self.visit(ctx.expr(1))
            op = ctx.relop().getText()

            temp = self.new_temp()
            self.emit(f"{temp} = {a} {op} {b}")
            return temp

        if ctx.AND():
            a = self.visit(ctx.condition(0))
            b = self.visit(ctx.condition(1))
            t = self.new_temp()
            self.emit(f"{t} = {a} && {b}")
            return t

        if ctx.OR():
            a = self.visit(ctx.condition(0))
            b = self.visit(ctx.condition(1))
            t = self.new_temp()
            self.emit(f"{t} = {a} || {b}")
            return t

        if ctx.NOT():
            val = self.visit(ctx.condition(0))
            t = self.new_temp()
            self.emit(f"{t} = !{val}")
            return t

        if ctx.TRUE():
            return "1"

        if ctx.FALSE():
            return "0"

        if ctx.condition():
            return self.visit(ctx.condition(0))

        return "0"
    
    # ================= VALUE EXPR =================
    def visitValueExpr(self, ctx):

        if ctx.ternaryExpr():
            return self.visit(ctx.ternaryExpr())

        return self.visit(ctx.expr())
    

    # ================= TERNARY =================
    def visitTernaryExpr(self, ctx):

        cond = self.visit(ctx.condition())

        Ltrue = self.new_label()
        Lend = self.new_label()

        temp = self.new_temp()

        self.emit(f"if {cond} goto {Ltrue}")

        false_val = self.visit(ctx.expr(1))
        self.emit(f"{temp} = {false_val}")
        self.emit(f"goto {Lend}")

        self.emit(f"{Ltrue}:")

        true_val = self.visit(ctx.expr(0))
        self.emit(f"{temp} = {true_val}")

        self.emit(f"{Lend}:")

        return temp



    # ================= IF =================
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

    # ================= WHILE =================
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

    # ================= PRINT =================
    def visitPrintStmt(self, ctx):
        val = self.visit(ctx.expr())
        self.emit(f"print {val}")

    # ================= RETURN =================
    def visitReturnStmt(self, ctx):
        if ctx.expr():
            val = self.visit(ctx.expr())
            self.emit(f"return {val}")
        else:
            self.emit("return")

    # ================= FUNCIONES =================
    def visitFunctionDecl(self, ctx):
        nombre = ctx.VAR().getText()

        self.emit(f"begin_func {nombre}")

        if ctx.paramList():
            for p in ctx.paramList().param():
                self.emit(f"param {p.VAR().getText()}")

        self.visit(ctx.block())

        self.emit(f"end_func {nombre}")

    def visitFunctionCall(self, ctx):
        nombre = ctx.VAR().getText()

        args = []
        if ctx.argList():
            args = [self.visit(e) for e in ctx.argList().expr()]

        for arg in args:
            self.emit(f"arg {arg}")

        temp = self.new_temp()
        self.emit(f"{temp} = call {nombre}, {len(args)}")
        return temp