from compiler.gramatica_v4Visitor import gramatica_v4Visitor

class TACGenerator(gramatica_v4Visitor):

    def __init__(self):
        self.code = []
        self.temp_count = 0
        self.label_count = 0

        self.loop_stack = []  # para break / continue
        self.structs = {}  # para definir estructuras
        self.variables = {}  # para almacenar variables y sus tipos

    # UTILIDADES
    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def emit(self, line):
        self.code.append(line)

    # ROOT
    def visitRoot(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitStructDecl(self, ctx):
        nombre = ctx.VAR().getText()
        offset = 0
        self.structs[nombre] = {}   # 🔥 IMPORTANTE
        self.emit(f"struct {nombre}")
        for field in ctx.structField():
            campo = field.VAR().getText()
            self.structs[nombre][campo] = offset  # 🔥 MAPA REAL
            self.emit(f"field {campo} offset {offset}")
            offset += 4
        self.emit(f"end_struct {nombre}")
    
    # DECLARACIÓN
    def visitDeclaration(self, ctx):
        self.visit(ctx.declarationStatement())

    def visitDeclarationStatement(self, ctx):
        nombre = ctx.VAR().getText()
        tipo = ctx.tipo().getText()
        self.variables[nombre] = tipo

        if ctx.arrayLiteral():
            valores = [self.visit(e) for e in ctx.arrayLiteral().expr()]
            self.emit(f"{nombre} = [{', '.join(valores)}]")

        elif ctx.valueExpr():
            val = self.visit(ctx.valueExpr())
            self.emit(f"{nombre} = {val}")

    # ASIGNACIÓN
    def visitSimpleAssign(self, ctx):
        nombre = ctx.VAR().getText()
        val    = self.visit(ctx.expr())
        self.emit(f"{nombre} = {val}")

    def visitFieldAssign(self, ctx):
        struct_name = ctx.VAR()[0].getText()
        field_name  = ctx.VAR()[1].getText()
        val         = self.visit(ctx.expr())
        struct_type = self.variables[struct_name]
        offset      = self.structs[struct_type][field_name]
        self.emit(f"{struct_name}[{offset}] = {val}")

    # EXPRESIONES
    def visitExpr(self, ctx):

        # LITERALES
        if ctx.NUM():
            return ctx.NUM().getText()

        if ctx.FLOAT():
            return ctx.FLOAT().getText()

        if ctx.STRING():
            return ctx.STRING().getText()

        if ctx.TRUE():
            return "true"

        if ctx.FALSE():
            return "false"

        # ARRAY ACCESS
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '[':
            nombre = ctx.VAR().getText()
            index = self.visit(ctx.expr(0))

            temp = self.new_temp()
            self.emit(f"{temp} = {nombre}[{index}]")
            return temp

        # STRUCT FIELD ACCESS
        if ctx.fieldAccess():
            return self.visit(ctx.fieldAccess())
        
        # VARIABLE
        if ctx.VAR():
            return ctx.VAR().getText()

        # FUNCTION CALL
        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        # OPERACIONES
        if len(ctx.expr()) == 2:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()

            temp = self.new_temp()
            self.emit(f"{temp} = {left} {op} {right}")
            return temp

        # PARENTESIS
        if ctx.expr():
            return self.visit(ctx.expr(0))

    # CONDICIONES
    def visitCondition(self, ctx):

        if ctx.relop():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.relop().getText()

            temp = self.new_temp()
            self.emit(f"{temp} = {left} {op} {right}")
            return temp

        if ctx.AND():
            left = self.visit(ctx.condition(0))
            right = self.visit(ctx.condition(1))
            temp = self.new_temp()
            self.emit(f"{temp} = {left} && {right}")
            return temp

        if ctx.OR():
            left = self.visit(ctx.condition(0))
            right = self.visit(ctx.condition(1))
            temp = self.new_temp()
            self.emit(f"{temp} = {left} || {right}")
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

    # IF
    def visitIfStatement(self, ctx):

        cond = self.visit(ctx.condition())

        label_true = self.new_label()
        label_end = self.new_label()

        if ctx.ELSE():
            label_false = self.new_label()

            self.emit(f"if {cond} goto {label_true}")
            self.emit(f"goto {label_false}")

            # THEN
            self.emit(f"{label_true}:")
            self.visit(ctx.block(0))
            self.emit(f"goto {label_end}")

            # ELSE
            self.emit(f"{label_false}:")
            self.visit(ctx.block(1))

        else:
            self.emit(f"if {cond} goto {label_true}")
            self.emit(f"goto {label_end}")

            self.emit(f"{label_true}:")
            self.visit(ctx.block(0))

        self.emit(f"{label_end}:")

    # WHILE
    def visitWhileStatement(self, ctx):

        label_cond = self.new_label()
        label_body = self.new_label()
        label_end = self.new_label()

        self.emit(f"{label_cond}:")

        cond = self.visit(ctx.condition())

        self.emit(f"if {cond} goto {label_body}")
        self.emit(f"goto {label_end}")

        # LOOP STACK
        self.loop_stack.append({
            "break": label_end,
            "continue": label_cond
        })

        # BODY
        self.emit(f"{label_body}:")
        self.visit(ctx.block())
        self.emit(f"goto {label_cond}")

        self.loop_stack.pop()

        self.emit(f"{label_end}:")

    # FOR
    def visitForStatement(self, ctx):

        label_cond = self.new_label()
        label_body = self.new_label()
        label_update = self.new_label()
        label_end = self.new_label()

        # INIT
        if ctx.forInit():

            if ctx.forInit().declarationStatement():
                self.visit(ctx.forInit().declarationStatement())

            elif ctx.forInit().assignmentStatement():
                self.visit(ctx.forInit().assignmentStatement())

        # COND
        self.emit(f"{label_cond}:")

        if ctx.condition():

            cond = self.visit(ctx.condition())

            self.emit(f"if {cond} goto {label_body}")
            self.emit(f"goto {label_end}")

        else:
            self.emit(f"goto {label_body}")

        # LOOP STACK
        self.loop_stack.append({
            "break": label_end,
            "continue": label_update
        })

        # BODY
        self.emit(f"{label_body}:")
        self.visit(ctx.block())

        # UPDATE
        self.emit(f"{label_update}:")

        if ctx.forUpdate():
            self.visit(ctx.forUpdate().assignmentStatement())

        self.emit(f"goto {label_cond}")

        self.loop_stack.pop()

        self.emit(f"{label_end}:")

    # BREAK / CONTINUE
    def visitBreakStmt(self, ctx):
        target = self.loop_stack[-1]["break"]
        self.emit(f"goto {target}")

    def visitContinueStmt(self, ctx):
        target = self.loop_stack[-1]["continue"]
        self.emit(f"goto {target}")

    def visitSwitchStatement(self, ctx):

        valor_switch = self.visit(ctx.expr())

        end_label = self.new_label()

        self.loop_stack.append({
            "break": end_label,
            "continue": end_label
        })

        for case_ctx in ctx.caseClause():

            valor_case = self.visit(case_ctx.literal())

            case_label = self.new_label()

            self.emit(
                f"if {valor_switch} == {valor_case} goto {case_label}"
            )

            self.emit(f"{case_label}:")

            for stmt in case_ctx.statement():
                self.visit(stmt)

        if ctx.defaultClause():

            default_label = self.new_label()

            self.emit(f"{default_label}:")

            for stmt in ctx.defaultClause().statement():
                self.visit(stmt)

        self.loop_stack.pop()

        self.emit(f"{end_label}:")

    # FUNCIONES
    def visitFunctionDecl(self, ctx):

        nombre = ctx.VAR().getText()

        self.emit(f"begin_func {nombre}")

        # PARAMS
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
            self.emit(f"param {arg}")

        temp = self.new_temp()
        self.emit(f"{temp} = call {nombre}, {len(args)}")

        return temp

    # RETURN
    def visitReturnStmt(self, ctx):

        if ctx.expr():
            val = self.visit(ctx.expr())
            self.emit(f"return {val}")
        else:
            self.emit("return")

    # PRINT
    def visitPrintStmt(self, ctx):

        val = self.visit(ctx.expr())
        self.emit(f"print {val}")

    # IMPORT (fase futura)
    def visitImportStmt(self, ctx):
        return
    
    def visitFieldAccess(self, ctx):
        var_name = ctx.VAR()[0].getText()
        field_name = ctx.VAR()[1].getText()
        struct_type = self.variables.get(var_name)
        if struct_type is None:
            raise Exception(f"{var_name} no está declarado")
        struct_def = self.structs.get(struct_type)
        if struct_def is None:
            raise Exception(f"{struct_type} no es un struct")
        if field_name not in struct_def:
            raise Exception(f"{field_name} no existe en {struct_type}")
        offset = struct_def[field_name]
        temp = self.new_temp()
        self.emit(f"{temp} = {var_name}[{offset}]")
        return temp