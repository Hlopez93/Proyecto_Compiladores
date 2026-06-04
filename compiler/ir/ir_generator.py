from llvmlite import ir
from compiler.gramatica_v4Visitor import gramatica_v4Visitor

class IRGenerator(gramatica_v4Visitor):

    def __init__(self):
        self.module = ir.Module(name="module")

        self.module.triple = "x86_64-pc-linux-gnu"

        self.builder = None
        self.func = None

        self.variables = {}
        self.functions = {}

        self.loop_stack = []

        printf_type = ir.FunctionType(
            ir.IntType(32),
            [ir.IntType(8).as_pointer()],
            var_arg=True
        )
        self.printf = ir.Function(self.module, printf_type, name="printf")

    # ================= ROOT =================
    def visitRoot(self, ctx):

        func_type = ir.FunctionType(ir.IntType(32), [])
        self.func = ir.Function(self.module, func_type, name="main")

        block = self.func.append_basic_block("entry")
        self.builder = ir.IRBuilder(block)

        for stmt in ctx.statement():
            self.visit(stmt)

        self.builder.ret(ir.Constant(ir.IntType(32), 0))

    # ================= TIPOS =================
    def get_type(self, tipo):
        t = tipo.getText()

        if t == "int":
            return ir.IntType(32)
        if t == "float":
            return ir.DoubleType()
        if t == "bool":
            return ir.IntType(1)
        if t == "string":
            return ir.IntType(8).as_pointer()

        if "[]" in t:
            return ir.IntType(32).as_pointer()

        return ir.VoidType()

    # ================= DECLARACION =================
    def visitDeclaration(self, ctx):
        self.visit(ctx.declarationStatement())

    def visitDeclarationStatement(self, ctx):

        nombre = ctx.VAR().getText()
        llvm_type = self.get_type(ctx.tipo())

        ptr = self.builder.alloca(llvm_type, name=nombre)
        self.variables[nombre] = ptr

        if ctx.arrayLiteral():
            values = [self.visit(e) for e in ctx.arrayLiteral().expr()]
            array_type = ir.ArrayType(ir.IntType(32), len(values))

            array = self.builder.alloca(array_type)

            for i, val in enumerate(values):
                ptr_elem = self.builder.gep(array, [
                    ir.Constant(ir.IntType(32), 0),
                    ir.Constant(ir.IntType(32), i)
                ])
                self.builder.store(val, ptr_elem)

            ptr_cast = self.builder.bitcast(array, ir.IntType(32).as_pointer())
            self.builder.store(ptr_cast, ptr)

        elif ctx.expr():
            val = self.visit(ctx.expr())
            self.builder.store(val, ptr)

    # ================= ASIGNACION =================
    def visitAssignment(self, ctx):
        self.visit(ctx.assignmentStatement())

    def visitAssignmentStatement(self, ctx):
        nombre = ctx.VAR().getText()
        val = self.visit(ctx.expr())
        self.builder.store(val, self.variables[nombre])

    # ================= EXPRESIONES =================
    def visitExpr(self, ctx):
        # expr SUM term  |  expr RES term
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr())
            right = self.visit(ctx.term())
            op = ctx.getChild(1).getText()

            if op == '+':
                return self.builder.add(left, right)
            if op == '-':
                return self.builder.sub(left, right)

        # just a term
        return self.visit(ctx.term())

    def visitTerm(self, ctx):
        # term MUL/DIV/MOD factor
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.term())
            right = self.visit(ctx.factor())
            op = ctx.getChild(1).getText()

            if op == '*':
                return self.builder.mul(left, right)
            if op == '/':
                return self.builder.sdiv(left, right)
            if op == '%':
                return self.builder.srem(left, right)

        # just a factor
        return self.visit(ctx.factor())

    def visitFactor(self, ctx):
        # NUM
        if ctx.NUM():
            return ir.Constant(ir.IntType(32), int(ctx.NUM().getText()))

        # FLOAT
        if ctx.FLOAT():
            return ir.Constant(ir.DoubleType(), float(ctx.FLOAT().getText()))

        # STRING
        if ctx.STRING():
            return self.create_string(ctx.STRING().getText()[1:-1])

        # BOOL
        if ctx.TRUE():
            return ir.Constant(ir.IntType(1), 1)
        if ctx.FALSE():
            return ir.Constant(ir.IntType(1), 0)

        # Array access: VAR '[' expr ']'  — check BEFORE plain VAR
        if ctx.getChildCount() == 4:
            arr_ptr = self.builder.load(self.variables[ctx.VAR().getText()])
            index = self.visit(ctx.expr())
            elem_ptr = self.builder.gep(arr_ptr, [index])
            return self.builder.load(elem_ptr)

        # Function call — check BEFORE plain VAR
        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        # Plain variable
        if ctx.VAR():
            ptr = self.variables[ctx.VAR().getText()]
            return self.builder.load(ptr)

        # Parenthesized expression: '(' expr ')'
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())

        raise Exception(f"Factor IR no soportado: {ctx.getText()}")

    # ================= CONDICIONES =================
    def visitCondition(self, ctx):

        if ctx.AND():
            return self.builder.and_(self.visit(ctx.condition(0)), self.visit(ctx.condition(1)))

        if ctx.OR():
            return self.builder.or_(self.visit(ctx.condition(0)), self.visit(ctx.condition(1)))

        if ctx.NOT():
            return self.builder.not_(self.visit(ctx.condition(0)))

        if ctx.relop():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.relop().getText()
            return self.builder.icmp_signed(op, left, right)

        if ctx.TRUE():
            return ir.Constant(ir.IntType(1), 1)
        if ctx.FALSE():
            return ir.Constant(ir.IntType(1), 0)

        # PAI condition PAD
        return self.visit(ctx.condition(0))

    # ================= IF =================
    def visitIfStatement(self, ctx):

        cond = self.visit(ctx.condition())

        then_block = self.func.append_basic_block("then")
        else_block = self.func.append_basic_block("else") if ctx.ELSE() else None
        merge = self.func.append_basic_block("ifend")

        if else_block:
            self.builder.cbranch(cond, then_block, else_block)
        else:
            self.builder.cbranch(cond, then_block, merge)

        self.builder.position_at_start(then_block)
        self.visit(ctx.block(0))
        if not self.builder.block.is_terminated:
            self.builder.branch(merge)

        if else_block:
            self.builder.position_at_start(else_block)
            self.visit(ctx.block(1))
            if not self.builder.block.is_terminated:
                self.builder.branch(merge)

        self.builder.position_at_start(merge)

    # ================= WHILE =================
    def visitWhileStatement(self, ctx):

        cond_block = self.func.append_basic_block("while_cond")
        body_block = self.func.append_basic_block("while_body")
        end_block = self.func.append_basic_block("while_end")

        self.builder.branch(cond_block)

        self.builder.position_at_start(cond_block)
        cond = self.visit(ctx.condition())
        self.builder.cbranch(cond, body_block, end_block)

        self.builder.position_at_start(body_block)

        self.loop_stack.append({
            "break": end_block,
            "continue": cond_block
        })

        self.visit(ctx.block())

        self.loop_stack.pop()

        if not self.builder.block.is_terminated:
            self.builder.branch(cond_block)

        self.builder.position_at_start(end_block)

    # ================= BREAK / CONTINUE =================
    def visitBreakStmt(self, ctx):
        target = self.loop_stack[-1]["break"]
        self.builder.branch(target)

        new_block = self.func.append_basic_block("after_break")
        self.builder.position_at_start(new_block)

    def visitContinueStmt(self, ctx):
        target = self.loop_stack[-1]["continue"]
        self.builder.branch(target)

        new_block = self.func.append_basic_block("after_continue")
        self.builder.position_at_start(new_block)

    # ================= FUNCIONES =================
    def visitFunctionDecl(self, ctx):

        nombre = ctx.VAR().getText()
        ret_type = self.get_type(ctx.tipo())

        param_types = []
        param_names = []

        if ctx.paramList():
            for p in ctx.paramList().param():
                param_types.append(self.get_type(p.tipo()))
                param_names.append(p.VAR().getText())

        func_type = ir.FunctionType(ret_type, param_types)
        func = ir.Function(self.module, func_type, name=nombre)

        self.functions[nombre] = func

        prev_builder = self.builder
        prev_func = self.func
        prev_vars = self.variables

        self.func = func
        self.variables = {}

        block = func.append_basic_block("entry")
        self.builder = ir.IRBuilder(block)

        for i, arg in enumerate(func.args):
            arg.name = param_names[i]
            ptr = self.builder.alloca(arg.type)
            self.builder.store(arg, ptr)
            self.variables[arg.name] = ptr

        self.visit(ctx.block())

        if not self.builder.block.is_terminated:
            if isinstance(ret_type, ir.VoidType):
                self.builder.ret_void()
            else:
                self.builder.ret(ir.Constant(ret_type, 0))

        self.builder = prev_builder
        self.func = prev_func
        self.variables = prev_vars

    def visitReturnStmt(self, ctx):
        if ctx.expr():
            self.builder.ret(self.visit(ctx.expr()))
        else:
            self.builder.ret_void()

    def visitFunctionCall(self, ctx):

        func = self.functions[ctx.VAR().getText()]
        args = []

        if ctx.argList():
            args = [self.visit(e) for e in ctx.argList().expr()]

        return self.builder.call(func, args)

    # ================= PRINT =================
    def visitPrintStmt(self, ctx):

        val = self.visit(ctx.expr())

        if isinstance(val.type, ir.IntType) and val.type.width == 32:
            fmt = self.create_string("%d\n")
            self.builder.call(self.printf, [fmt, val])

        elif isinstance(val.type, ir.IntType) and val.type.width == 1:
            val32 = self.builder.zext(val, ir.IntType(32))
            fmt = self.create_string("%d\n")
            self.builder.call(self.printf, [fmt, val32])

        elif isinstance(val.type, ir.DoubleType):
            fmt = self.create_string("%f\n")
            self.builder.call(self.printf, [fmt, val])

        elif isinstance(val.type, ir.PointerType):
            fmt = self.create_string("%s\n")
            self.builder.call(self.printf, [fmt, val])

    # ================= STRING =================
    def create_string(self, text):
        text_bytes = bytearray(text.encode("utf8")) + b'\00'
        string_type = ir.ArrayType(ir.IntType(8), len(text_bytes))

        global_str = ir.GlobalVariable(self.module, string_type, name=f"str_{len(self.module.globals)}")
        global_str.global_constant = True
        global_str.initializer = ir.Constant(string_type, text_bytes)

        return self.builder.bitcast(global_str, ir.IntType(8).as_pointer())

    # ================= SWITCH / CASE ★ IMPLEMENTACIÓN =================
    def visitSwitchStatement(self, ctx):
        ctrl_val = self.visit(ctx.expr())

        # La instruccion switch de LLVM requiere un entero — si viene i1 (bool) lo extendemos
        if isinstance(ctrl_val.type, ir.IntType) and ctrl_val.type.width == 1:
            ctrl_val = self.builder.zext(ctrl_val, ir.IntType(32))

        end_block = self.func.append_basic_block("switch_end")

        # Si hay default, crea su bloque; si no, el default salta directo al end
        if ctx.defaultClause():
            default_block = self.func.append_basic_block("switch_default")
        else:
            default_block = end_block

        # Instruccion switch nativa de LLVM
        sw = self.builder.switch(ctrl_val, default_block)

        # Crear un bloque por cada case y registrar su valor en la switch table
        case_blocks = []
        for case_clause in ctx.caseClause():
            lit = case_clause.literal()
            if lit.NUM():
                case_val = ir.Constant(ir.IntType(32), int(lit.NUM().getText()))
            elif lit.FLOAT():
                # LLVM switch solo acepta enteros; convertimos el float a bits enteros
                import struct
                bits = struct.unpack('q', struct.pack('d', float(lit.FLOAT().getText())))[0]
                case_val = ir.Constant(ir.IntType(64), bits)
            else:
                case_val = ir.Constant(ir.IntType(32), 0)

            blk = self.func.append_basic_block(f"switch_case_{len(case_blocks)}")
            sw.add_case(case_val, blk)
            case_blocks.append(blk)

        # Empujar end_block para que break dentro de un case sepa a donde saltar
        self.loop_stack.append({"break": end_block, "continue": end_block})

        # Generar cuerpo de cada case
        for i, (case_clause, blk) in enumerate(zip(ctx.caseClause(), case_blocks)):
            self.builder.position_at_start(blk)
            for stmt in case_clause.statement():
                self.visit(stmt)
            # fall-through si no hubo break explicito
            if not self.builder.block.is_terminated:
                if i + 1 < len(case_blocks):
                    self.builder.branch(case_blocks[i + 1])
                elif ctx.defaultClause():
                    self.builder.branch(default_block)
                else:
                    self.builder.branch(end_block)

        # Generar cuerpo del default
        if ctx.defaultClause():
            self.builder.position_at_start(default_block)
            for stmt in ctx.defaultClause().statement():
                self.visit(stmt)
            if not self.builder.block.is_terminated:
                self.builder.branch(end_block)

        self.loop_stack.pop()
        self.builder.position_at_start(end_block)

    def visitCaseClause(self, ctx):
        pass  # visitado inline en visitSwitchStatement

    def visitDefaultClause(self, ctx):
        pass  # visitado inline en visitSwitchStatement